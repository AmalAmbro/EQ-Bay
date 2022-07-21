from django import forms
from django.forms.widgets import TextInput, FileInput

from .models import Category, Product, ProductVariant, ProductVariantImg

from dal import autocomplete


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','industry','parent']
        widgets = {
            'name':TextInput(attrs={'class': 'form-control','placeholder':'Category or Sub-Category'}),
            'industry':autocomplete.ModelSelect2(url='dashboard:autocomplete_industry',attrs={'class': 'form-control','data-placeholder': 'Choose Industry', 'data-minimum-input-length': 0}),
            'parent':autocomplete.ModelSelect2(url='dashboard:autocomplete_category',attrs={'class': 'form-control','data-placeholder': 'Choose Category', 'data-minimum-input-length': 0}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['is_featured','name','category','image','description','features','specifications','dimensions','test_method','product_resources']
        widgets = {
            'name':TextInput(attrs={'class': 'form-control','placeholder':'Category or Sub-Category'}),
            'category':autocomplete.ModelSelect2(url='dashboard:autocomplete_category',attrs={'class': 'form-control','data-placeholder': 'Choose Category', 'data-minimum-input-length': 0}),
            'description':TextInput(attrs={'class': 'form-control','placeholder':'Product description'}),
            'features':TextInput(attrs={'class': 'form-control','placeholder':'Product features'}),
            'specifications':TextInput(attrs={'class': 'form-control','placeholder':'Product specifications'}),
            'dimensions':TextInput(attrs={'class': 'form-control','placeholder':'Product dimensions'}),
            'test_method':TextInput(attrs={'class': 'form-control','placeholder':'Product test method'}),
            'product_resources':TextInput(attrs={'class': 'form-control','placeholder':'Product resources'}),
            'image':FileInput(attrs={'class': 'form-control'})

        }


class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['product','model_name']
        widgets = {
            'product':autocomplete.ModelSelect2(url='category:autocomplete_product',attrs={'class': 'form-control','data-placeholder': 'Choose Product', 'data-minimum-input-length': 0}),
            'model_name':TextInput(attrs={'class': 'form-control','placeholder':'Model name'}),
        }

class ProductVariantImgForm(forms.ModelForm):
    class Meta:
        model = ProductVariantImg
        fields = ['image', 'product_variant']
        widgets = {
            'product_variant':autocomplete.ModelSelect2(url='customers:autocomplete_productvariant',attrs={'class': 'form-control','data-placeholder': 'Choose Product Variant', 'data-minimum-input-length': 0}),
            'image':FileInput(attrs={'class': 'form-control'})
        }
