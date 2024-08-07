from typing import Any
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

class Sub_category(models.Model):
    sub_category_id = models.AutoField(primary_key=True)
    sub_category_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category')

    class Meta:
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return self.sub_category_name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to='images/')
    product_count = models.CharField(max_length=50)
    sub_category = models.ForeignKey(Sub_category, on_delete=models.CASCADE,related_name='product')

   
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name
