from django.urls import path, re_path

from .views import ProductAutoComplete, delete_product_variant, delete_product_variant_img, delete_products, edit_product_variant, edit_product_variant_img, product_variant, product_variant_img, products

app_name = 'category'

urlpatterns = [
    re_path(r'^autocomplete/products/$', ProductAutoComplete.as_view(), name='autocomplete_product'),
]
