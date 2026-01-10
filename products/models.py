from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
class Size(models.Model):
    GENDER_CHOICES = [
        ('boy', 'Boy'),
        ('girl', 'Girl'),
        ('unisex', 'Unisex'),
    ]

    age_group = models.CharField(max_length=50)
    size_label = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.age_group} - {self.size_label} ({self.gender})"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    stock = models.PositiveIntegerField()
    sizes = models.ManyToManyField(Size, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

