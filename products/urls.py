from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('category/<slug:slug>/', views.category_products, name='category_products'),
]
