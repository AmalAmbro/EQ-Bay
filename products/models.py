import uuid

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from main.models import BaseModel
from ckeditor.fields import RichTextField


class Category(MPTTModel, BaseModel):
    name = models.CharField(max_length=128)
    industry = models.ForeignKey('web.Industry', on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='self')

    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name


class Product(BaseModel):
    is_featured = models.BooleanField(default=False)
    name = models.CharField(max_length=128)
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE)
    image = models.FileField(upload_to='product/')
    description = RichTextField()
    features = RichTextField(null=True, blank=True)
    specifications = RichTextField(null=True, blank=True)
    dimensions = RichTextField(null=True, blank=True)
    test_method = RichTextField(null=True, blank=True)
    product_resources = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.name

class ProductVariant(BaseModel):
    model_name = models.CharField(max_length=64)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.model_name

class ProductVariantImg(BaseModel):
    image = models.FileField(upload_to='productVariants/')
    product_variant = models.ForeignKey('products.ProductVariant', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product_variant)
