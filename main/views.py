from django.http import HttpResponse
from django.shortcuts import *
from django.core import serializers
from urllib3 import request
from main.models import Product
from main.forms import ProductForm
def show_main(request):
    context = {
        'nama_aplikasi' : 'Cihuy United',
        'npm' : '2406345186',
        'name': 'Muhammad Derriel Ramadhan',
        'class': 'PBP F',
        'products': Product.objects.all()
    }
    
    return render(request, "main.html", context)

def create_product(request):
        form = ProductForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('main:show_main')
            else:
                new_form = ProductForm()
                context = {
                'form': new_form,
                'error': form.errors
            }
            return render(request, 'create_product.html', context)
        elif request.method == 'GET':
            context = {
                'form': form
            }
            return render(request, 'create_product.html', context)
    
        return HttpResponse(status = 404 )
    
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_details.html", context)


def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")


def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)


def show_json_by_id(request, product_id):
    try:
        product_item = Product.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [product_item])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)