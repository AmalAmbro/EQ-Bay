from django.db import models
from django.core.validators import RegexValidator

from main.models import BaseModel

from main.variables import phone_regex


class Customer(BaseModel):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(validators=[RegexValidator(r'^[0-9]{9,16}$', message="Phone no : 9876543210")], max_length=30)
    name = models.CharField(max_length=128, null=True, blank=True)
    password = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Customers"
    
    def __str__(self):
        return str(self.user)

class OTPRecords(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=30, validators=[RegexValidator(r'^[0-9]{9,16}$', message="only digits and no country codes")])
    otp = models.CharField(max_length=20, validators=[RegexValidator(r'^\d{4}$', message="otp should be 4 digits")])
    attempts = models.PositiveIntegerField(default=0)
    is_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "OTP Records"
    
    def __str__(self):
        return self.phone

class CustomerAddress(BaseModel):
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    # phone_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}$', message="Phone No: +000 9876543210")
    phone = models.CharField(validators=[phone_regex] ,max_length=20)
    email = models.EmailField()
    address = models.TextField(max_length=400)
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    is_business = models.BooleanField(default=False)
    gstin = models.CharField(max_length=64, null=True, blank=True)
    vat_no = models.CharField(max_length=64, null=True, blank=True)
    designation = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Customer Addresses"

    def __str__(self):
        return self.first_name

class RfqList(BaseModel):
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    product_variant = models.ForeignKey('products.ProductVariant', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "RfqList"

    def __str__(self):
        return self.customer

class QuoteRequest(BaseModel):
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    # phone_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}$', message="Phone No: +000 9876543210")
    phone = models.CharField(validators=[phone_regex] ,max_length=20)
    email = models.EmailField()
    address = models.TextField(max_length=400)
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    is_business = models.BooleanField(default=False)
    gstin = models.CharField(max_length=64, null=True, blank=True)
    vat_no = models.CharField(max_length=64, null=True, blank=True)
    designation = models.CharField(max_length=64, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Quote Requests"

    def __str__(self):
        return self.first_name
    
class QuoteRequestItem(models.Model):
    id = models.AutoField(primary_key=True)
    quote_request = models.ForeignKey('customers.QuoteRequest', on_delete=models.CASCADE)
    product_variant = models.ForeignKey('products.ProductVariant', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Quote Request Items"

    def __str__(self):
        return str(self.id)
    
