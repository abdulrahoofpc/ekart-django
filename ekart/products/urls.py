from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('product',views.list,name='product'),
    path('product_details/<pk>',views.product,name='product_details')
]