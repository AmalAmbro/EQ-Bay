from datetime import datetime
import json
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from main.functions import generate_form_errors, get_auto_id
from products.form import CategoryForm
from products.models import Category

from web.form import ContactDetailsForm, EnquiryForm, IndustryForm, InnovationForm
from web.models import ContactDetails, Enquiry, Industry, Innovation

from dal import autocomplete


#Industry#
def industry(request):
    industries = Industry.objects.all()
    if (industries):
        context = {
            'page_title':'Industry | EQ-Bay',
            'industries': industries,
            'message': False,
        }
        return render(request, 'admin_panel/industry/industry.html', context=context)
    else:
        context = {
            'page_title':'Industry | EQ-Bay',
            'message':'Industry List',
            'menu':'Industry',
            'create_link': reverse('dashboard:industry_create')
        }
        return render(request, 'admin_panel/nodata.html', context=context)

def industry_view(request, id):
    data = Industry.objects.get(id=id)
    context = {
        'page_title':data.name,
        'data':data,
    }
    return render(request, 'admin_panel/industry/industry_view.html', context=context)

def industry_create(request):
    form = IndustryForm()
    if request.method == 'POST':
        form = IndustryForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auto_id = get_auto_id(Industry)
            instance.creator = request.user
            instance.updater = request.user

            name = instance.name
            if not Industry.objects.filter(name = name).exists():
                instance.save()
                message  ="Industry Successfully Created"
                response_data = {
                "title":"Successfully Created",
                "message":message,
                "status":"success",
                "redirect":False,
                "redirect_url":"/",
            }
            else:
                message = "Industry already exists."
                response_data = {
                    "title":"Industry already exists",
                    "message":message,
                    "status":"warning",
                    "redirect":False,
                    "redirect_url":"/",
                }
            
        else:
            message = generate_form_errors(form)
            response_data = {
                "title":"Form Error",
                "message":message,
                "status":"error",
                "redirect":False,
                "redirect_url":"/",
            }
        
        return HttpResponse(json.dumps(response_data),content_type="application/json")
    else:
        context = {
            'page_title':'Create',
            'form':form,
        }
        return render(request, 'admin_panel/industry/industry_create.html', context = context)

def delete_industries(request,id):
    data = Industry.objects.get(id=id)
    data.delete()
    
    response_data = {
        "title":"Successfully Deleted",
        "message":"Industry Successfully Deleted",
        "status":"success",
        "redirect":True,
        "redirect_url":reverse('dashboard:industry'),
    }
        
    return HttpResponse(json.dumps(response_data),content_type="application/json")

def edit_industries(request, id):
    instance = get_object_or_404(Industry, id=id)
    if request.method == 'POST':
        form = IndustryForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.updater = request.user
            instance.date_updated = datetime.now()
            instance.save()
            message = "Industry Successfully Updated"
            response_data = {
                "title":"Successfuly Updated",
                "message":message,
                "status":"success",
                "redirect":False,
                "redirect_url":"/",
            }
            
        else:
            message = generate_form_errors(form)
            response_data = {
                "title":"Form Error",
                "message":message,
                "status":"error",
                "redirect":False,
                "redirect_url":"/",
            }
        
        return HttpResponse(json.dumps(response_data),content_type="application/json")
            
        
    else:
        form = IndustryForm(instance=instance)
        
    context = {
        'page_title':'Industry | Edit',
        'form': form,
        'id':id,
        'instance':instance,
    }
    return render(request, 'admin_panel/industry/industry_edit.html', context=context)

class IndustryAutoComplete(autocomplete.Select2QuerySetView):
   def get_queryset(self):
       if not self.request.user.is_authenticated:
           return Industry.objects.none()

       items = Industry.objects.all()

       if self.q:
           items = items.filter(Q(auto_id__istartswith=self.q) | Q(name__istartswith=self.q))

       return items


#Contact#
def contact_details(request):
    contacts = ContactDetails.objects.all()
    if request.method == 'POST':
        form = ContactDetailsForm(request.POST)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auto_id = get_auto_id(ContactDetails)
            instance.creator = request.user
            instance.updater = request.user
            
            instance.save()
            message = "Contact details were saved"            
            

        else:
            message = generate_form_errors(form)

    else:  
        form = ContactDetailsForm()
        message = False
    context = {
        'title':'Contacts | EQ-Bay',
        'form': form,
        'contacts': contacts,
        'message': message
    }
    return render(request, 'admin_panel/contacts/contact.html', context=context)


def delete_contacts(request):
    id_list = request.GET.getlist('id')
    # print(id_list)
    for id in id_list:
        obj = ContactDetails.objects.get(pk=id)
        obj.delete()

    form = ContactDetailsForm()
    contacts = ContactDetails.objects.all()
    context = {
        'title':'Contacts | EQ-Bay',
        'form': form,
        'contacts': contacts,
        'message': False,
    }
    return render(request, 'admin_panel/contacts/contact.html', context=context)

def edit_contacts(request, id):
    instance = get_object_or_404(ContactDetails, id=id)
    if request.method == 'POST':
        form = ContactDetailsForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.updater = request.user
            instance.date_updated = datetime.now()
            instance.save()
            message = "Updated the details succesfully"
            form = ContactDetailsForm()

        else:
            message = generate_form_errors(form)

    else:
        form = ContactDetailsForm(instance=instance)
        message = False
    context = {
        'title':'Contacts | Edit',
        'form': form,
        'id':id,
        'message': message,
    }
    return render(request, 'admin_panel/contacts/contact_edit.html', context=context)

#Enquiries#
def enquiries(request):
    enquiries = Enquiry.objects.all()

    if (enquiries):
        context = {
            'page_title':'Enquiries | EQ-Bay',
            'enquiries': enquiries,
            'message': False,
        }
        return render(request, 'admin_panel/enquiry/enquiry.html', context=context)
    else:
        context = {
            'page_title':'Enquiries | EQ-Bay',
            'message':'Enquiry List',
        }
        return render(request, 'admin_panel/nodata.html', context=context)

def enquiry_create(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auto_id = get_auto_id(Enquiry)
            instance.save()
            message = "Enquiry submitted"            
            form = EnquiryForm()

            
        else:
            message = generate_form_errors(form)

    else:  
        form = EnquiryForm()
        message=False
    context = {
        'title':'Enquiries | EQ-Bay',
        'form': form,
        'message': message,
    }
    return render(request, 'admin_panel/enquiry/enquiry_create.html', context=context)

def enquiry_view(request, id):
    data = Enquiry.objects.get(id=id)

    context = {
        'page_title':'Enquiry',
        'data':data,
    }
    return render(request, 'admin_panel/enquiry/enquiry_view.html', context=context)




def delete_enquiry(request, id):
    data = Enquiry.objects.get(id=id)
    data.delete()

    response_data = {
        "title":"Successfully Deleted",
        "message":"Enquiry Deleted Successfully",
        "status":"success",
        "redirect":True,
        "redirect_url":reverse('dashboard:enquiries'),
    }
        
    return HttpResponse(json.dumps(response_data),content_type="application/json")

def edit_enquiry(request, id):
    instance = get_object_or_404(Enquiry, id=id)
    if request.method == 'POST':
        form = EnquiryForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            message = "Updated the details succesfully"
            form = EnquiryForm()

        else:
            message = generate_form_errors(form)
    else:
        form = EnquiryForm(instance=instance)
        message = False

    context = {
        'title':'Enquiries Edit | EQ-Bay',
        'form': form,
        'id':id,
        'message': message,
    }
    return render(request, 'admin_panel/enquiry/enquiry_edit.html', context=context)

#Innovations#
def innovations(request):
    innovations = Innovation.objects.all()
    if (innovations):
        context = {
            'page_title':'Innovations | EQ-Bay',
            'innovations': innovations,
        }
        return render(request, 'admin_panel/innovation/innovation.html', context=context)
    else:
        context = {
            'page_title':'Innovations | EQ-Bay',
            'message':'Innovation List',
            'create_link': reverse('dashboard:create_innovation'),
            'menu':'Innovation',
        }
        return render(request, 'admin_panel/nodata.html', context=context)
    

def create_innovation(request):
    if request.method == 'POST':
        form = InnovationForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auto_id = get_auto_id(Innovation)
            instance.creator = request.user
            instance.updater = request.user
            
            instance.save()
            message = "Innovation Created successfully"
            response_data = {
                "title":"Successfully Created",
                "message":message,
                "status":"success",
                "redirect":False,
                "redirect_url":"/home",
            }

        else:
            message = generate_form_errors(form)
            response_data = {
                "title":"Form Error",
                "message":message,
                "status":"error",
                "redirect":False,
                "redirect_url":"/home",
            }
        
        return HttpResponse(json.dumps(response_data),content_type="application/json")
            
    else:  
        form = InnovationForm()
        message = False
    context = {
        'page_title':'Innovations | EQ-Bay',
        'form': form,
        'message': message,
    }
    return render(request, 'admin_panel/innovation/innovation_create.html', context=context)

def view_innovation(request, id):
    data = Innovation.objects.get(id=id)

    context = {
        'page_title':"Innovation",
        'data':data,
    }
    return render(request, 'admin_panel/innovation/innovation_view.html', context=context)

def delete_innovations(request,id):
    data = Innovation.objects.get(id=id)
    data.delete()

    response_data = {
        "title":"Successfully Deleted",
        "message":"Innovation Deleted Successfully",
        "status":"success",
        "redirect":True,
        "redirect_url":reverse('dashboard:innovations'),
    }
    return HttpResponse(json.dumps(response_data),content_type="application/json")


def edit_innovation(request, id):
    instance = get_object_or_404(Innovation, id=id)
    if request.method == 'POST':
        form = InnovationForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            message = "Innovation Updated succesfully"
            response_data = {
                "title":"Successfully Updated",
                "message":message,
                "status":"success",
                "redirect":False,
                "redirect_url":"/",
            }
            
        else:
            message = generate_form_errors(form)
            response_data = {
                "title":"Form Error",
                "message":message,
                "status":"error",
                "redirect":False,
                "redirect_url":"/",
            }
        
        return HttpResponse(json.dumps(response_data),content_type="application/json")
    else:
        form = InnovationForm(instance=instance)
        message = False

    context = {
        'page_title':'Innovation Edit',
        'form': form,
        'id':id,
        'message': message,
        'instance':instance,
    }
    return render(request, 'admin_panel/innovation/innovation_edit.html', context=context)

#Category#
def category(request):
    categories = Category.objects.all()
    if (categories):
        context = {
            'page_title':'Category | EQ-Bay',
            'categories': categories,
            'message': False,
        }
        return render(request, 'admin_panel/category/category.html', context=context)
    else:
        context = {
            'page_title':'Category | EQ-Bay',
            'message':'Category List',
            'menu':'Category',
            'create_link': reverse('dashboard:category_create')
        }
        return render(request, 'admin_panel/nodata.html', context=context)

def category_create(request):
    
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auto_id = get_auto_id(Category)
            instance.creator = request.user
            instance.updater = request.user
            name = instance.name
            industry = instance.industry

            if not Category.objects.filter(name=name).filter(industry=industry).exists():
                instance.save()

                response_data = {
                "title":"Successfully Created",
                "message":"Category Successfully Created",
                "status":"success",
                "redirect":False,
                "redirect_url":"/home",
            }
            else:
                message = "Category already exists."
                response_data = {
                    "title":"Category already exists",
                    "message":message,
                    "status":"warning",
                    "redirect":False,
                    "redirect_url":"/home",
                }
            
        else:
            message = generate_form_errors(form)
            response_data = {
                "title":"Form Error",
                "message":message,
                "status":"error",
                "redirect":False,
                "redirect_url":"/home",
            }
        
        return HttpResponse(json.dumps(response_data),content_type="application/json")
    
    form = CategoryForm()
    message = False
    context = {
        'page_title':'Categories | EQ-Bay',
        'form': form,
        'message':message,
    }
    return render(request, 'admin_panel/category/category_create.html', context = context)

def category_view(request, id):
    data = Category.objects.get(id=id)
    context = {
        'page_title':'Category',
        'data':data,
    }
    return render(request, 'admin_panel/category/category_view.html', context=context)

def edit_category(request, id):
    instance = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.updater = request.user
            instance.date_updated = datetime.now()
            instance.save()
            response_data = {
                "title":"Successfully Updated",
                "message":"Category Successfully Updated",
                "status":"success",
                "redirect":False,
                "redirect_url":"/",
            }
            
        else:
            message = generate_form_errors(form)
            response_data = {
                "title":"Form Error",
                "message":message,
                "status":"error",
                "redirect":False,
                "redirect_url":"/",
            }
        
        return HttpResponse(json.dumps(response_data),content_type="application/json")
            
        
    else:
        form = CategoryForm(instance=instance)
        
    context = {
        'page_title':'Category',
        'form': form,
        'id':id,
    }
    return render(request, 'admin_panel/category/category_edit.html', context=context)

def delete_category(request, id):
    data = Category.objects.get(id=id)
    data.delete()

    response_data = {
        "title":"Successfully Deleted",
        "message":"Category Successfully Deleted",
        "status":"success",
        "redirect":True,
        "redirect_url":reverse('dashboard:category'),
    }
        
    return HttpResponse(json.dumps(response_data),content_type="application/json")

class CategoryAutoComplete(autocomplete.Select2QuerySetView):
   def get_queryset(self):
       if not self.request.user.is_authenticated:
           return Category.objects.none()

       items = Category.objects.all()

       if self.q:
           items = items.filter(Q(auto_id__istartswith=self.q) | Q(name__istartswith=self.q))

       return items
