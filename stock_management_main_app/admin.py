from django.contrib import admin
from .models import Category, Sub_category, Product
from django.utils.html import format_html
from django import forms


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    def save_model(self, request, obj, form, change):
        # Check if a product with the same name already exists
        obj.category_name = obj.category_name.lower()
        existing_product = Category.objects.filter(category_name=obj.category_name).first()
        if existing_product and not change:
            pass
        else:
            # If the product doesn't exist or we're updating an existing product
            super().save_model(request, obj, form, change)


class SubCategoryAdmin(admin.ModelAdmin):
    # list_display = ('sub_category_name',)
    def save_model(self, request, obj, form, change):
        # Check if a product with the same name already exists
        obj.sub_category_name = obj.sub_category_name.lower()
        # print(subcategory)
        existing_product = Sub_category.objects.filter(sub_category_name=obj.sub_category_name).first()
        print(existing_product)
        if existing_product and not change:
            pass
        else:
            # If the product doesn't exist or we're updating an existing product
            super().save_model(request, obj, form, change)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_image')
    # list_display = ('name', 'description', 'price', 'product_count', 'image_tag')

    def save_model(self, request, obj, form, change):
        # Check if a product with the same name already exists
        obj.product_name = obj.product_name.lower()
        existing_product = Product.objects.filter(product_name=obj.product_name).first()
        if existing_product and not change:
            existing_product.product_count = int(existing_product.product_count)
            # If the product already exists and we're not updating an existing product
            existing_product.product_count += int(obj.product_count)
            existing_product.save()
        else:
            # If the product doesn't exist or we're updating an existing product
            super().save_model(request, obj, form, change)

    def product_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.image.url))
        return "-"
    product_image.short_description = 'Image'

admin.site.register(Product, ProductAdmin)

# Register your models here.
admin.site.register(Category, CategoryAdmin),
admin.site.register(Sub_category, SubCategoryAdmin),
# admin.site.register(Product) 