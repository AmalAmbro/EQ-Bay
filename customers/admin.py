from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','auto_id','creator','updater','date_added','date_updated','is_deleted','user','phone','name','password']

admin.site.register(Customer, CustomerAdmin)

class OTPRecordsAdmin(admin.ModelAdmin):
    list_display = ['id','phone','otp','attempts', 'is_verified']

admin.site.register(OTPRecords, OTPRecordsAdmin)

class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['id','auto_id','creator','updater','date_added','date_updated','is_deleted','customer','first_name','last_name','phone','email','address','company_name','city','pincode','country','is_business','gstin','vat_no','designation']

admin.site.register(CustomerAddress, CustomerAddressAdmin)

class RfqListAdmin(admin.ModelAdmin):
    list_display = ['id','auto_id','creator','updater','date_added','date_updated','is_deleted','customer','product_variant','quantity']

admin.site.register(RfqList, RfqListAdmin)

class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ['id','auto_id','creator','updater','date_added','date_updated','is_deleted','customer','first_name','last_name','phone','email','address','company_name','city','pincode','country','is_business','gstin','vat_no','designation']

admin.site.register(QuoteRequest, QuoteRequestAdmin)

class QuoteRequestItemAdmin(admin.ModelAdmin):
    list_display = ['id','quote_request','product_variant','quantity']

admin.site.register(QuoteRequestItem, QuoteRequestItemAdmin)
