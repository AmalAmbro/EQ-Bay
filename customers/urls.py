from django import views
from django.urls import path, re_path

from customers.views import CustomerAutoComplete, QuoteRequestAutoComplete, customer_details, delete_customer, delete_customer_details, delete_otp, delete_quote, delete_quote_item_request, delete_rfq, edit_customer, edit_customer_details, edit_quote, edit_quote_item_request, edit_rfq, otprecords, quote_item_requests ,rfqlist
from products.views import ProductVariantAutoComplete


app_name = "customers"

urlpatterns = [
    # path('', customer, name='customer'),
    path('delete/<uuid:id>/', delete_customer, name='delete_customer'),
    path('edit/<uuid:id>/', edit_customer, name='edit_customer'),
    path('otp/', otprecords, name='otprecords'),
    path('otp/delete/<int:id>/', delete_otp, name='delete_otp'),
    path('details/', customer_details, name='customer_details'),
    path('details/delete/<uuid:id>/', delete_customer_details, name='delete_customer_details'),
    path('details/edit/<uuid:id>/', edit_customer_details, name='edit_customer_details'),
    path('item-requests/', quote_item_requests, name='quote_item_requests'),
    path('item-requests/delete/<int:id>/', delete_quote_item_request, name='delete_quote_item_requests'),
    path('item-requests/edit/<int:id>/', edit_quote_item_request, name='edit_quote_item_requests'),
    path('rfqlist/', rfqlist, name='rfqlist'),
    path('rfqlist/delete/<uuid:id>/', delete_rfq, name='delete_rfq'),
    path('rfqlist/edit/<uuid:id>/', edit_rfq, name='edit_rfq'),
    #autocomplete urls#
    re_path(r'^autocomplete/$', CustomerAutoComplete.as_view(), name='autocomplete_customer'),
    re_path(r'^quote-request/autocomplete/$', QuoteRequestAutoComplete.as_view(), name='autocomplete_quoterequest'),
    re_path(r'^product-variant/autocomplete/$', ProductVariantAutoComplete.as_view(), name='autocomplete_productvariant'),
]