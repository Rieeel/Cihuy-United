from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import *
from django.core import serializers
from urllib3 import request
from main.models import Product
from main.forms import ProductForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json


@login_required(login_url='/main/login/')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
    context = {
        'nama_aplikasi' : 'Cihuy United',
        'npm' : '2406345186',
        'name':  request.user.username,
        'class': 'PBP F',
        'products': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect('main:show_main')

    return render(request, 'create_product.html', {'form': form})


    
@login_required(login_url='/main/login/')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product_id': product.id,
        'product': product
    }

    return render(request, "product_details.html", context)


def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'user': product.user.username if product.user else None,
            'description': product.description,
            'category': product.category,
            'category_id': product.category,
            'thumbnail': product.thumbnail,
            'price': product.price,
            'stock': product.stock,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'created_at': product.created_at.isoformat() if hasattr(product, 'created_at') else None,
            'views': product.views if hasattr(product, 'views') else 0,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)


def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)


def show_json_by_id(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price': product.price, 
            'stock': product.stock, 
            'views': product.views if hasattr(product, 'views') else 0,
            'category': product.category,
            'category_id': product.category,
            'thumbnail': product.thumbnail if product.thumbnail else None,
            'is_featured': product.is_featured,
            'user': product.user.username if product.user else None,
            'user_name': product.user.username if product.user else 'Anonymous',
            'user_id': product.user_id,
            'created_at': product.created_at.isoformat() if hasattr(product, 'created_at') and product.created_at else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

@csrf_exempt
@require_POST
def register_ajax(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Your account has been successfully created!'})
    else:
        errors = {}
        for field, error_list in form.errors.items():
            errors[field] = [str(error) for error in error_list]
        return JsonResponse({'success': False, 'errors': errors}, status=400)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_exempt
@require_POST
def login_ajax(request):
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return JsonResponse({
            'success': True, 
            'message': 'Login successful!',
            'redirect_url': reverse("main:show_main")
        })
    else:
        errors = {}
        for field, error_list in form.errors.items():
            errors[field] = [str(error) for error in error_list]
        return JsonResponse({'success': False, 'errors': errors}, status=400)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      
      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    category = strip_tags(request.POST.get("category"))
    thumbnail = strip_tags(request.POST.get("thumbnail"))
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user
    price = int(request.POST.get("price", 0))
    stock = int(request.POST.get("stock", 0))

    new_product = Product(
        name=name,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        price=price,
        stock=stock,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def edit_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this product.")

    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    category = strip_tags(request.POST.get("category"))
    thumbnail = strip_tags(request.POST.get("thumbnail"))
    is_featured = request.POST.get("is_featured") == 'on'
    price = int(request.POST.get("price", 0))
    stock = int(request.POST.get("stock", 0))

    product.name = name
    product.description = description
    product.category = category
    product.thumbnail = thumbnail
    product.is_featured = is_featured
    product.price = price
    product.stock = stock
    product.save()

    return HttpResponse(b"UPDATED", status=200)

@csrf_exempt
@require_POST
def delete_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this product.")

    product.delete()
    return HttpResponse(b"DELETED", status=200)

@csrf_exempt
def create_product_flutter(request):
    # Endpoint untuk integrasi Flutter (POST JSON)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)

        name = strip_tags(data.get("title") or data.get("name") or "")
        description = strip_tags(data.get("content") or data.get("description") or "")
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)
        price = data.get("price", 0)
        stock = data.get("stock", 0)
        user = request.user if request.user.is_authenticated else None

        new_product = Product(
            name=name,
            description=description,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            price=price or 0,
            stock=stock or 0,
            user=user
        )
        new_product.save()

        return JsonResponse({"status": "success", "id": str(new_product.id)}, status=201)
    return JsonResponse({"status": "error", "message": "Invalid method"}, status=405)

@csrf_exempt
def delete_product_flutter(request, id):
    if request.method == 'POST':
        try:
            # Gunakan filter karena ID adalah UUID
            product = Product.objects.get(pk=id)
            
            # Verifikasi ownership
            if product.user != request.user:
                return JsonResponse({
                    "status": "error",
                    "message": "Unauthorized"
                }, status=403)
            
            product.delete()
            return JsonResponse({"status": "success"}, status=200)
            
        except Product.DoesNotExist:
            return JsonResponse({
                "status": "error",
                "message": "Product not found"
            }, status=404)
    
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)

@csrf_exempt
def edit_product_flutter(request, id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product = Product.objects.get(pk=id)
            
            # Verifikasi ownership
            if product.user != request.user:
                return JsonResponse({
                    "status": "error",
                    "message": "Unauthorized"
                }, status=403)
            
            # Update fields
            product.name = data["name"]
            product.price = data["price"]
            product.description = data["description"]
            product.thumbnail = data["thumbnail"]
            product.category = data["category"]
            product.is_featured = data.get("is_featured", False)
            product.save()
            
            return JsonResponse({"status": "success"}, status=200)
            
        except Product.DoesNotExist:
            return JsonResponse({
                "status": "error",
                "message": "Product not found"
            }, status=404)
    
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)



