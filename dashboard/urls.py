from django.urls import path, re_path
from customers.views import create_quote_request, customer_view, delete_customer, delete_quote, edit_quote, quote_request_view, quote_requests
from dashboard.views import CategoryAutoComplete, IndustryAutoComplete, category, category_create, category_view, contact_details, create_innovation, delete_category, delete_contacts, delete_enquiry, delete_industries, delete_innovations, edit_category, edit_contacts, edit_enquiry, edit_industries, edit_innovation, enquiries, enquiry_view, industry, industry_create, industry_view, innovations, view_innovation
from products.views import create_product_var_img, create_product_variant, delete_product_variant, delete_product_variant_img, delete_products, edit_product_variant, edit_product_variant_img, product_var_img_view, product_variant, product_variant_img, product_variant_view, products, products_create, products_edit, products_view


app_name = 'dashboard'

urlpatterns = [
    #industry#
    path('industry/', industry,name='industry'),
    path('industry/create/', industry_create,name='industry_create'),
    path('industry/<uuid:id>/', industry_view,name='industry_view'),
    path('industry/delete/<uuid:id>/', delete_industries, name='delete_industries'),
    path('industry/edit/<uuid:id>/', edit_industries, name='edit_industry'),

    #category#
    path('category/',category, name='category'),
    path('category/create/',category_create, name='category_create'),
    path('category/view/<uuid:id>/',category_view, name='view_category'),
    path('category/edit/<uuid:id>/',edit_category, name='edit_category'),
    path('category/delete/<uuid:id>/',delete_category, name='delete_category'),

    #product#
    path('products/',products, name='products'),
    path('products/create',products_create, name='products_create'),
    path('products/view/<uuid:id>/',products_view, name='products_view'),
    path('products/delete/<uuid:id>/',delete_products, name='delete_products'),
    path('products/edit/<uuid:id>/',products_edit, name='products_edit'),

    #product variant#
    path('product-variants/',product_variant, name='product_variants'),
    path('product-variants/create/',create_product_variant, name='product_variants_create'),
    path('product-variants/view/<uuid:id>/',product_variant_view, name='product_variant_view'),
    path('product-variants/delete/<uuid:id>/',delete_product_variant, name='delete_product_variants'),
    path('product-variants/edit/<uuid:id>/',edit_product_variant, name='edit_product_variants'),

    #product variant image#
    path('product-variants-img/',product_variant_img, name='product_variants_img'),
    path('product-variants-img/view/<uuid:id>/',product_var_img_view, name='product_variants_img_view'),
    path('product-variants-img/create/',create_product_var_img, name='create_product_variants_img'),
    path('product-variants-img/delete/<uuid:id>/',delete_product_variant_img, name='delete_product_variants_img'),
    path('product-variants-img/edit/<uuid:id>/',edit_product_variant_img, name='edit_product_variants_img'),

    #quote requests#
    path('requests/', quote_requests, name='quote_requests'),
    path('requests/view/<uuid:id>/', quote_request_view, name='quote_request_view'),
    path('requests/create/', create_quote_request, name='create_quote_request'),
    path('requests/delete/<uuid:id>/', delete_quote, name='delete_quote'),
    path('requests/edit/<uuid:id>/', edit_quote, name='edit_quote'),

    #enquiries#
    path('enquiries/', enquiries, name='enquiries'),
    path('enquiries/view/<uuid:id>/', enquiry_view, name='view_enquiry'),
    path('enquiries/delete/<uuid:id>/', delete_enquiry, name='delete_enquiry'),

    #contact#
    path('contacts/', contact_details, name='contacts'),
    path('contacts/delete/', delete_contacts, name='delete_contacts'),
    path('contacts/edit/<uuid:id>/', edit_contacts, name='edit_contacts'),

    #innovation#
    path('innovations/', innovations,name='innovations'),
    path('innovation/create/', create_innovation, name='create_innovation'),
    path('innovation/view/<uuid:id>/', view_innovation, name='view_innovation'),
    path('innovation/delete/<uuid:id>/', delete_innovations, name='delete_innovations'),
    path('innovation/edit/<uuid:id>/', edit_innovation, name='edit_innovation'),

    #customer#
    path('customers/<uuid:id>/', customer_view, name='customers'),
    path('customers/delete/<uuid:id>/', delete_customer, name='delete_customer'),

    #auto complete urls#
    re_path(r'^autocomplete/industry/$', IndustryAutoComplete.as_view(), name='autocomplete_industry'),
    re_path(r'^autocomplete/categories/$', CategoryAutoComplete.as_view(), name='autocomplete_category'),
]
