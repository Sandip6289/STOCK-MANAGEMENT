from django.shortcuts import render, redirect
from django.views import View
from .models import Category, Sub_category, Product
# Create your views here.

class Index(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):
        return render(request, 'index.html')
    

class ShowProduct(View):
    def get(self, request):
        try: 
            products = Product.objects.all()
        except:
            return render(request, 'show_product.html', {'error': "error loading products"})
        if products:
            return render(request, 'show_product.html', {'products': products})
        
        return render(request, 'show_product.html')
    

class AddProduct(View):
    def get(self, request):
        try:
            sub_category = Sub_category.objects.all()
            return render(request, "add_product.html", {'sub_category':sub_category})
        except:
            pass

        return render(request, "add_product.html")
    

class AddCategory(View):
    def get(self, request):
        return render(request, 'add_category.html')
    

class StoreProductInDB(View):
    def post(self, request):
        print(request.POST['subcategory'])
        try:
            product_name = request.POST['productname'].lower()
            product_count = request.POST['productcount'].lower()
            try:
                product_image = request.FILES['productimage']
            except:
                product_image = None
            sub_category = Sub_category.objects.get(sub_category_name=request.POST['subcategory'])
            try:
                product = Product.objects.get(product_name=product_name)
                if product:
                    product.product_count = int(product.product_count)
                    product.product_count += int(product_count)
                    print(product.product_count)
                    product.save()
                else:
                    product = Product.objects.create(product_name=product_name, product_count=product_count, product_image=product_image, sub_category=sub_category)
                    product.save()

            except Exception as e:
                print(e)
                print(request.POST['subcategory'])
                product = Product.objects.create(product_name=product_name, product_count=product_count, product_image=product_image, sub_category=sub_category)
                product.save()

            return redirect('show_product')
        except:
            print("Error saving product")

            return redirect('index')


class StoreCategoryInDB(View):
    def post(self, request):
        print(request.POST['categoryname'])
        try:
            category_name = request.POST['categoryname'].lower()
            
            if category_name is not None:
                try:
                    existing_category = Category.objects.get(category_name=category_name)
                    print(existing_category)
                except Exception as e:
                    category = Category.objects.create(category_name=category_name)
                    category.save()
            return redirect('show_product')
        except:
            print("Error saving Category")

            return redirect('index')


class AddSubCategory(View):
    def get(self, request):
        try:
            category = Category.objects.all()
            return render(request, "add_sub_category.html", {'category':category})
        except:
            pass

        return render(request, "add_sub_category.html")
    
class StoreSubCategoryInDB(View):
    def post(self, request):
        print(request.POST['subcategoryname'])
        try:
            sub_category_name = request.POST['subcategoryname'].lower()
            category = Category.objects.get(category_name=request.POST['category'])
            if sub_category_name is not None:
                try:
                    existing_category = Sub_category.objects.get(sub_category_name=sub_category_name)
                    print(existing_category)
                except Exception as e:
                    subcategory = Sub_category.objects.create(sub_category_name=sub_category_name, category=category)
                    subcategory.save()
            return redirect('show_product')
        except:
            print("Error saving Sub Category")

            return redirect('index')