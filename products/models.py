from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories'
    )

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} → {self.name}"
        return self.name

    
class Size(models.Model):
    CATEGORY_CHOICES = [
        ('kids', 'Kidswear'),
        ('women', "Women's Wear"),
        ('men', "Men's Wear"),
    ]

    GENDER_CHOICES = [
        ('boy', 'Boy'),
        ('girl', 'Girl'),
        ('unisex', 'Unisex'),
        ('women', 'Women'),
        ('men', 'Men'),
    ]

    category_type = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES
    )
    label = models.CharField(max_length=20)  # XS, S, M, L, XL, 28, 30
    age_group = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )  # only for kids
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    def __str__(self):
        if self.category_type == 'kids':
            return f"{self.label} - {self.age_group}"
        return f"{self.label} ({self.category_type})"


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    logo = models.ImageField(upload_to='brands/', blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    stock = models.PositiveIntegerField()
    sizes = models.ManyToManyField(Size, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

