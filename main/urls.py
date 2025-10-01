from django.urls import path
from main.views import (show_main, 
                        create_products, 
                        show_products, 
                        show_xml, 
                        show_json, 
                        show_xml_by_id, 
                        show_json_by_id,
                        register,
                        login_user,
                        logout_user,
                        edit_product,
                        delete_news)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'), 
    path('create-products/', create_products, name='create_products'),
    path('products/<uuid:id>/', show_products, name='show_products'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('products/<uuid:id>/edit/', edit_product, name='edit_product'),
    path('products/<uuid:id>/delete', delete_news, name='delete_product'),
]