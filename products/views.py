from datetime import datetime

import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.urls import reverse

from main.functions import generate_form_errors, get_auto_id

from products.models import Category, Product, ProductVariant, ProductVariantImg
from .form import ProductForm, ProductVariantForm, ProductVariantImgForm

from dal import autocomplete


#Product#
def products(request):
    products = Product.objects.all()

    if (products):
        context = {
            'page_title':'Products | EQ-Bay',
            'products': products,
            'message': False,
        }
        return render(request, 'admin_panel/products/products.html', context=context)
    else:
        context = {
            'page_title':'Products | EQ-Bay',
            'message':'Products List',
            'create_link': reverse('dashboard:products_create'),
            'menu':'Product',
        }
        return render(request, 'admin_panel/nodata.html', context=context)

def products_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auto_id = get_auto_id(Product)
            instance.creator = request.user
            instance.updater = request.user
            instance.save()
            message = "Product Successfully Created"
            response_data = {
                "title":"Successfully Created",
                "message":message,
                "status":"success",
                "redirect":False,
                "redirect_url":"/home",
            }

        else:
            message = generate_form_errors(form)
            response_data = {
                "title":"Form Error",
                "message":message,
                "status":"error",
                "redirect":False,
                "redirect_url":"/home",
            }
        
        return HttpResponse(json.dumps(response_data),content_type="application/json")
    else:
        form = ProductForm()
        message = False
    context = {
        'page_title':'Products | EQ-Bay',
        'form': form,
        'message': message,
        'products': products
    }
    return render(request, 'admin_panel/products/product_create.html', context=context)

def products_view(request, id):
    data = Product.objects.get(id=id)
    context = {
        'page_title':data.name,
        'data':data,
    }
    return render(request, 'admin_panel/products/product_view.html', context=context)


def delete_products(request, id):
    
    data = Product.objects.get(id=id)
    data.delete()

    response_data = {
        "title":"Successfully Deleted",
        "message":"Product Deleted Successfully",
        "status":"success",
        "redirect":True,
        "redirect_url":reverse('dashboard:products'),
    }
    return HttpResponse(json.dumps(response_data),content_type="application/json")

def products_edit(request, id):
    instance = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.date_updated = datetime.now()
            instance.save()
            message = "Product updated successfully"
            response_data = {
                "title":"Successfully Updated",
                "message":message,
                "status":"success",
                "redirect":False,
                "redirect_url":"/",
            }
        else:
            message = generate_form_errors(form)
            response_data = {
                "title":"Form Error",
                "message":message,
                "status":"error",
                "redirect":False,
                "redirect_url":"/",
            }
        return HttpResponse(json.dumps(response_data),content_type="application/json")

    else:
        form = ProductForm(instance=instance)
        message = False
    context = {
        'page_title':'Product | Edit',
        'form': form,
        'id':id,
        'message': message,
        'instance':instance,
    }
    return render(request, 'admin_panel/products/product_edit.html', context=context)

class ProductAutoComplete(autocomplete.Select2QuerySetView):
   def get_queryset(self):
       if not self.request.user.is_authenticated:
           return Product.objects.none()

       items = Product.objects.all()

       if self.q:
           items = items.filter(Q(auto_id__istartswith=self.q) | Q(name__istartswith=self.q))

       return items


#Product Variant#
def product_variant(request):
    product_variants = ProductVariant.objects.all()

    if (product_variants):
        context = {
            'page_title':'Product Variants | EQ-Bay',
            'product_variants': product_variants,
            'message': False,
        }
        return render(request, 'admin_panel/product-variants/product_variant.html', context=context)
    else:
        context = {
            'page_title':'Product Variants | EQ-Bay',
            'message':'Product Variants List',
            'create_link': reverse('dashboard:product_variants_create'),
            'menu':'Product Variant',
        }
        return render(request, 'admin_panel/nodata.html', context=context)

def product_variant_view(request,id):
    data = ProductVariant.objects.get(id=id)
    context = {
        'page_title':data.model_name,
        'data':data,
    }
    return render(request, 'admin_panel/product-variants/product_variant_view.html', context=context)

def create_product_variant(request):
    if request.method == "POST":
        form = ProductVariantForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auto_id = get_auto_id(ProductVariant)
            instance.creator = request.user
            instance.updater = request.user
            instance.save()
            message = "Product Variant Created successfully"
            response_data = {
                "title":"Successfully Created",
                "message":message,
                "status":"success",
                "redirect":False,
                "redirect_url":"/home",
            }

        else:
            message = generate_form_errors(form)
            response_data = {
                "title":"Form Error",
                "message":message,
                "status":"error",
                "redirect":False,
                "redirect_url":"/home",
            }
        
        return HttpResponse(json.dumps(response_data),content_type="application/json")

    else:
        form = ProductVariantForm()
        message = False
    context = {
        'page_title':'Product Variants | EQ-Bay',
        'form':form,
    }
    return render(request, 'admin_panel/product-variants/product_variant_create.html', context=context)

def delete_product_variant(request,id):
    data = ProductVariant.objects.get(id=id)
    data.delete()

    response_data = {
        "title":"Successfully Deleted",
        "message":"Product Variant Successfully Deleted",
        "status":"success",
        "redirect":True,
        "redirect_url":reverse('dashboard:product_variants'),
    }
    return HttpResponse(json.dumps(response_data),content_type="application/json")

def edit_product_variant(request, id):
    instance = get_object_or_404(ProductVariant, id=id)
    if request.method == 'POST':
        form = ProductVariantForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.date_updated = datetime.now()
            instance.save()
            message = "Product Variant Updated Successfully"
            response_data = {
                "title":"Successfully Updated",
                "message":message,
                "status":"success",
                "redirect":False,
                "redirect_url":"/",
            }
        else:
            message = generate_form_errors(form)
            response_data = {
                "title":"Form Error",
                "message":message,
                "status":"error",
                "redirect":False,
                "redirect_url":"/",
            }
        return HttpResponse(json.dumps(response_data),content_type="application/json")
    else:
        form = ProductVariantForm(instance=instance)
        message = False
    context = {
        'page_title':'Product Variants Image',
        'form': form,
        'id':id,
        'message': message,
    }
    return render(request, 'admin_panel/product-variants/product_variant_edit.html', context=context)

class ProductVariantAutoComplete(autocomplete.Select2QuerySetView):
   def get_queryset(self):
       if not self.request.user.is_authenticated:
           return ProductVariant.objects.none()

       items = ProductVariant.objects.all()

       if self.q:
           items = items.filter(Q(auto_id__istartswith=self.q) | Q(name__istartswith=self.q))

       return items


#Product Variant Img#
def product_variant_img(request):
    product_variants_img = ProductVariantImg.objects.all()

    if (product_variants_img):
        context = {
            'page_title':'Product Variants Images | EQ-Bay',
            'product_variants_imgs': product_variants_img,
            'message': False,
        }
        return render(request, 'admin_panel/product-variant-img/product_variant_img.html', context=context)
    else:
        context = {
            'page_title':'Product Variants Images | EQ-Bay',
            'message':'Product Variants Img List',
            'create_link': reverse('dashboard:create_product_variants_img'),
            'menu':'Product Variant Image',
        }
        return render(request, 'admin_panel/nodata.html', context=context)

def product_var_img_view(request, id):
    data = ProductVariantImg.objects.get(id=id)
    context = {
        'page_title':data.product_variant,
        'data':data,
    }
    return render(request, 'admin_panel/product-variant-img/product_var_img_view.html', context=context)

def create_product_var_img(request):
    if request.method == "POST":
        form = ProductVariantImgForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auto_id = get_auto_id(ProductVariantImg)
            instance.creator = request.user
            instance.updater = request.user
            instance.save()
            message = "Product Variant Image Created Successfully"
            response_data = {
                "title":"Successfully Created",
                "message":message,
                "status":"success",
                "redirect":False,
                "redirect_url":"/home",
            }

        else:
            message = generate_form_errors(form)
            response_data = {
                "title":"Form Error",
                "message":message,
                "status":"error",
                "redirect":False,
                "redirect_url":"/home",
            }
        
        return HttpResponse(json.dumps(response_data),content_type="application/json")

    else:
        form = ProductVariantImgForm()
        message = False
    context = {
        'page_title':'Product Variants Images | EQ-Bay',
        'form': form,
        'message': message,
    }
    return render(request, 'admin_panel/product-variant-img/product_variant_image_create.html', context = context)

def delete_product_variant_img(request, id):
    data = ProductVariantImg.objects.get(id=id)
    data.delete()

    response_data = {
        "title":"Successfully Deleted",
        "message":"Product Variant Image Deleted Successfully",
        "status":"success",
        "redirect":True,
        "redirect_url":reverse('dashboard:product_variants_img'),
    }
    return HttpResponse(json.dumps(response_data),content_type="application/json")

def edit_product_variant_img(request, id):
    instance = get_object_or_404(ProductVariantImg, id=id)
    if request.method == 'POST':
        form = ProductVariantImgForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.date_updated = datetime.now()
            instance.save()
            message = "Product Variant Image updated successfully"
            form = ProductVariantImgForm()
            response_data = {
                    "title":"Successfully Updated",
                    "message":message,
                    "status":"success",
                    "redirect":False,
                    "redirect_url":"/",
                }
        else:
            message = generate_form_errors(form)
            response_data = {
                "title":"Form Error",
                "message":message,
                "status":"error",
                "redirect":False,
                "redirect_url":"/",
            }
        return HttpResponse(json.dumps(response_data),content_type="application/json")
    else:
        form = ProductVariantImgForm(instance=instance)
        message = False
    context = {
        'page_title':'Product Variants Img | EQ-Bay',
        'form': form,
        'id':id,
        'message': message,
        'instance':instance,
    }
    return render(request, 'admin_panel/product-variant-img/product_variant_img_edit.html', context=context)
