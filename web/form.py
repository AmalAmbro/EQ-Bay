from django import forms
from django.forms.widgets import TextInput, Textarea, FileInput
from web.models import ContactDetails, Enquiry, Industry, Innovation


class IndustryForm(forms.ModelForm):
    class Meta:
        model = Industry
        fields = ['name','image']
        widgets = {
            'name':TextInput(attrs={'class': 'form-control','placeholder':'Name'}),
            'image':FileInput(attrs={'class': 'form-control'}),
        }
        
class ContactDetailsForm(forms.ModelForm):
    class Meta:
        model = ContactDetails
        fields = ['phone','address','email']
        widgets = {
            'phone':TextInput(attrs={'class': 'form-control','placeholder':'Enter your Contact No'}),
            'address':Textarea(attrs={'class': 'form-control','placeholder':'Enter your current address'}),
            'email':TextInput(attrs={'class': 'form-control','placeholder':'Enter your email'}),
        }


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name','phone','message','email']
        widgets = {
            'name':TextInput(attrs={'class': 'form-control','placeholder':'Enter your name'}),
            'phone':TextInput(attrs={'class': 'form-control','placeholder':'Enter your Contact No'}),
            'message':Textarea(attrs={'class': 'form-control','placeholder':'Enter your query'}),
            'email':TextInput(attrs={'class': 'form-control','placeholder':'Enter your email'}),
        }


class InnovationForm(forms.ModelForm):
    class Meta:
        model = Innovation
        fields = ['title','image','short_description','extra_content']
        widgets = {
            'title':TextInput(attrs={'class': 'form-control','placeholder':'Enter Title'}),
            'image':FileInput(attrs={'class': 'form-control',}),
            'short_description':Textarea(attrs={'class': 'form-control','placeholder':'Enter your query'}),
            'extra_content':Textarea(attrs={'class': 'form-control','placeholder':'Enter your email'}),
        }
