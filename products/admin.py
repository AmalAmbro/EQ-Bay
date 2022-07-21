from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','auto_id','creator','updater','date_added','date_updated','is_deleted','name','industry','parent']
    readonly_fields = ['date_added','date_updated']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','auto_id','creator','updater','date_added','date_updated','is_deleted','is_featured','name','category','image','description','features','specifications','dimensions','test_method','product_resources']
    readonly_fields = ['date_added','date_updated']

admin.site.register(Product, ProductAdmin)

class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['id','auto_id','creator','updater','date_added','date_updated','is_deleted','model_name','product']
    readonly_fields = ['date_added','date_updated']

admin.site.register(ProductVariant, ProductVariantAdmin)

class ProductVariantImgAdmin(admin.ModelAdmin):
    list_display = ['id','auto_id','creator','updater','date_added','date_updated','is_deleted','image','product_variant']
    readonly_fields = ['date_added','date_updated']

admin.site.register(ProductVariantImg, ProductVariantImgAdmin)
