from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
]
