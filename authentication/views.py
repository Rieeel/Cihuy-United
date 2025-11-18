from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login(request):
    # Mendukung form-encoded (default Django) atau JSON body dari Flutter
    if request.content_type == 'application/json':
        try:
            payload = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"status": False, "message": "Invalid JSON"}, status=400)
        username = payload.get('username', '')
        password = payload.get('password', '')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)

@csrf_exempt
def register(request):
    if request.method != 'POST':
        return JsonResponse({"status": False, "message": "Method not allowed"}, status=405)

    # Terima JSON atau form data
    if request.content_type == 'application/json':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"status": False, "message": "Invalid JSON"}, status=400)
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()
        email = data.get('email', '').strip()
    else:
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        email = request.POST.get('email', '').strip()

    errors = {}
    if not username:
        errors['username'] = 'Username wajib diisi.'
    if not password:
        errors['password'] = 'Password wajib diisi.'
    if User.objects.filter(username=username).exists():
        errors['username'] = 'Username sudah digunakan.'

    if errors:
        return JsonResponse({"status": False, "errors": errors}, status=400)

    user = User.objects.create_user(username=username, password=password, email=email)
    return JsonResponse({"status": True, "message": "Register sukses!", "username": user.username}, status=201)

@csrf_exempt
def logout(request):
    username = request.user.username if request.user.is_authenticated else ''
    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logged out successfully!"
        }, status=200)
    except Exception:
        return JsonResponse({
            "status": False,
            "message": "Logout failed."
        }, status=401)
