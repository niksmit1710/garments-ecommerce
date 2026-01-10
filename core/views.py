from django.shortcuts import render
from products.models import Category

def home(request):
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, 'home.html', {'categories': categories})
