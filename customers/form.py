from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from dal import autocomplete

from customers.models import Customer, CustomerAddress, OTPRecords, QuoteRequest, QuoteRequestItem, RfqList
from .users import UsernameField


# USER = User.objects.all()
# CUSTOMERS = Customer.objects.all()
# QUOTE_REQUESTS = QuoteRequest.objects.all()
# PRODUCT_VARIANTS = ProductVariant.objects.all()

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone','name','password']
        widgets = {
            # 'user':forms.Select(choices=USER, attrs={'placeholder':'User'}),
            'phone':TextInput(attrs={'class': 'form-control','placeholder':'Contact Number'}),
            'name':TextInput(attrs={'class': 'form-control','placeholder':'Name'}),
            'password':TextInput(attrs={'class': 'form-control','placeholder':'password'}),
        }

class CustomerAddressForm(forms.ModelForm):
    class Meta:
        model = CustomerAddress
        fields = ['customer','first_name','last_name','phone','email','address','company_name','city','pincode','country','is_business','gstin','vat_no','designation']
        widgets = {
            # 'customer':forms.Select(choices=CUSTOMERS, attrs={'placeholder':'Customer'}),
            'customers':autocomplete.ModelSelect2(url='customers:autocomplete_customer',attrs={'class': 'form-control','data-placeholder': 'Choose Customer', 'data-minimum-input-length': 0}),
            'first_name':TextInput(attrs={'class': 'form-control','placeholder':'First Name'}),
            'last_name':TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}),
            'phone':TextInput(attrs={'class': 'form-control','placeholder':'Contact Number'}),
            'email':TextInput(attrs={'class': 'form-control','placeholder':'Email Address'}),
            'address':Textarea(attrs={'class': 'form-control','placeholder':'Current Address'}),
            'company_name':TextInput(attrs={'placeholder':'Company Name'}),
            'city':TextInput(attrs={'class': 'form-control','placeholder':'City Located'}),
            'pincode':TextInput(attrs={'class': 'form-control','placeholder':'Pincode'}),
            'country':TextInput(attrs={'class': 'form-control','placeholder':'Country'}),
            'gstin':TextInput(attrs={'class': 'form-control','placeholder':'GSTIN'}),
            'vat_no':TextInput(attrs={'class': 'form-control','placeholder':'VAT NO'}),
            'designation':TextInput(attrs={'class': 'form-control','placeholder':'Designation'}),
        }

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['customer','first_name','last_name','phone','email','address','company_name','city','pincode','country','is_business','gstin','vat_no','designation']
        widgets = {
            # 'customer':forms.Select(choices=CUSTOMERS, attrs={'placeholder':'Customer'}),
            'customers':autocomplete.ModelSelect2(url='customers:autocomplete_customer',attrs={'class': 'form-control','data-placeholder': 'Choose Customer', 'data-minimum-input-length': 0}),
            'first_name':TextInput(attrs={'placeholder':'First Name'}),
            'last_name':TextInput(attrs={'placeholder':'Last Name'}),
            'phone':TextInput(attrs={'placeholder':'Contact Number'}),
            'email':TextInput(attrs={'placeholder':'Email Address'}),
            'address':Textarea(attrs={'placeholder':'Current Address'}),
            'company_name':TextInput(attrs={'placeholder':'Company Name'}),
            'city':TextInput(attrs={'placeholder':'City Located'}),
            'pincode':TextInput(attrs={'placeholder':'Pincode'}),
            'country':TextInput(attrs={'placeholder':'Country'}),
            'gstin':TextInput(attrs={'placeholder':'GSTIN'}),
            'vat_no':TextInput(attrs={'placeholder':'VAT NO'}),
            'designation':TextInput(attrs={'placeholder':'Designation'}),
        }

class QuoteRequestItemForm(forms.ModelForm):
    class Meta:
        model = QuoteRequestItem
        fields = ['quote_request','product_variant','quantity']
        widgets = {
            'quote_requests':autocomplete.ModelSelect2(url='customers:autocomplete_quoterequest',attrs={'class':'form-control','data-placeholder': 'Choose Quote Request', 'data-minimum-input-length': 0}),
            'product_variants':autocomplete.ModelSelect2(url='customers:autocomplete_productvariant',attrs={'class':'form-control','data-placeholder': 'Choose Product Variant', 'data-minimum-input-length': 0}),
            'quantity':TextInput(attrs={'placeholder':'Quantity'}),
        }
        

class OTPRecordsForm(forms.ModelForm):
    class Meta:
        model = OTPRecords
        fields = ['phone','otp']
        widgets = {
            'phone':TextInput(attrs={'placeholder':'Contact Number'}),
            'otp':TextInput(attrs={'placeholder':'Enter otp'}),
        }

class RfqListForm(forms.ModelForm):
    class Meta:
        model = RfqList
        fields = ['customer','product_variant','quantity']
        widgets = {
            'customers':autocomplete.ModelSelect2(url='customers:autocomplete_customer',attrs={'class': 'form-control','data-placeholder': 'Choose Customer', 'data-minimum-input-length': 0}),
            'product_variants':autocomplete.ModelSelect2(url='customers:autocomplete_productvariant',attrs={'class':'form-control','data-placeholder': 'Choose Product Variant', 'data-minimum-input-length': 0}),
            'quantity':TextInput(attrs={'placeholder':'Enter quantity'}),

        }

class RegistrationForm(UserCreationForm):
    """
    Form for registering a new user account.

    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.

    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.

    """
    required_css_class = 'required'
    first_name = forms.CharField(max_length=100, label=_("First Name"))
    last_name = forms.CharField(max_length=100, label=_("Last Name"))
    email = forms.EmailField(label=_("E-mail"))
    phone = forms.CharField(max_length=30, label=_("Phone"))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", 'phone', UsernameField())
