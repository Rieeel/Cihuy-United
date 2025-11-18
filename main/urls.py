from django import views
from django.urls import path
from main.views import delete_product_flutter, edit_product_flutter, show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id , register, login_user , logout_user, edit_product, delete_product, add_product_entry_ajax, edit_product_ajax, delete_product_ajax, register_ajax, login_ajax, create_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create/', create_product, name='create_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('products/xml/', show_xml, name='show_xml'),
    path('products/json/', show_json, name='show_json'),
    path('json/', show_json, name='show_json_short'),
    path('products/xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('products/json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id_short'),
    path('register/', register, name='register'),
    path('main/login/', login_user, name='login'),
    path('main/logout/', logout_user, name='logout'),
    path('products/<uuid:id>/edit', edit_product, name='edit_product'),
    path('products/<uuid:id>/delete', delete_product, name='delete_product'),
    path('create-product-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('edit-product-ajax/<str:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('delete-product-ajax/<str:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('register-ajax/', register_ajax, name='register_ajax'),
    path('login-ajax/', login_ajax, name='login_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('edit-flutter/<uuid:id>/', edit_product_flutter, name='edit_product_flutter'),
    path('delete-flutter/<uuid:id>/', delete_product_flutter, name='delete_product_flutter'),
]
