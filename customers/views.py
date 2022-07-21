from datetime import datetime
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import Q
from customers.form import CustomerAddressForm, CustomerForm, OTPRecordsForm, QuoteRequestForm, QuoteRequestItemForm, RfqListForm
from main.functions import decrypt_message, encrypt_message, generate_form_errors, get_auto_id, get_otp
from customers.models import Customer, CustomerAddress, OTPRecords, QuoteRequest, QuoteRequestItem, RfqList

from dal import autocomplete


def customer_view(request, id):
    data = Customer.objects.get(id=id)

    context = {
        'page_title':'Customer',
        'data':data,
    }
    return render(request, 'admin_panel/customers/customer/customer_view.html', context=context)

def customer_create(request):
    customers = Customer.objects.all()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.updater = request.user
            if not Customer.objects.filter(user = request.user):
                instance.user = request.user
                instance.auto_id = get_auto_id(Customer)
                password = instance.password
                instance.password = encrypt_message(password)
                instance.save()
                message = "User created successfully"
            else:
                message = "User already exists"
            form = CustomerForm()
        else:
            message = generate_form_errors(form)

    else:
        form = CustomerForm()
        message = False
    context = {
        'title': "Customer | EQ_Bay",
        'customers': customers,
        'form': form,
        'message': message,
        'customers': customers
    }
    return render(request, 'admin_panel/customers/customer/customer.html', context)

def delete_customer(request, id):
    data = Customer.objects.get(id=id)
    user = data.user
    user.delete()

    response_data = {
        "title":"Success",
        "message":"Customer deleted",
        "status":"success",
        "redirect":True,
        "redirect_url":reverse('main:index'),
    }
    return HttpResponse(json.dumps(response_data),content_type="application/json")

class CustomerAutoComplete(autocomplete.Select2QuerySetView):
   def get_queryset(self):
       if not self.request.user.is_authenticated:
           return Customer.objects.none()

       items = Customer.objects.all()

       if self.q:
           items = items.filter(Q(auto_id__istartswith=self.q) | Q(name__istartswith=self.q))

       return items


def edit_customer(request,id):
    instance = get_object_or_404(Customer, id=id)
    password = decrypt_message(instance.password)
    # print(password)
    instance.password = password
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.date_updated = datetime.now()
            instance.updater = request.user
            instance.password = encrypt_message(instance.password)
            instance.save()
            message = "Updated successfully"
        else:
            message = generate_form_errors(form)
    else:
        form = CustomerForm(instance=instance)
        message = False
    context = {
        'title':'Customer Edit | EQ-Bay',
        'message': message,
        'form': form,
        'id': id,
    }
    return render(request, 'admin_panel/customers/customer/customer_edit.html', context=context)

def otprecords(request):
    otps = OTPRecords.objects.all()
    if request.method == "POST":
        form = OTPRecordsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            otp = instance.otp
            attempts = instance.attempts
            phone = instance.phone
          
            if OTPRecords.objects.filter(phone = phone).exists():
                instance = get_object_or_404(OTPRecords, phone=phone)
                id = instance.id
                form = OTPRecordsForm(request.POST, instance=instance)
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.id = id
                    instance.otp = otp
                    instance.attempts = instance.attempts+1
                    message = "OTP created"  
                    instance.save()   
                else:
                    message = generate_form_errors(form)    

            else:
                instance.attempts = attempts+1
                instance.save()
                form = OTPRecordsForm()   
                message = "OTP created"         
        else:
            message = generate_form_errors(form)
    
    else:
        form = OTPRecordsForm()
        message = False
    context = {
        'title': 'OTP Records',
        'otps': otps,
        'form': form,
        'message': message,
    }
    return render(request, 'admin_panel/customers/otprecords/otp.html', context = context)


def delete_otp(request, id):
    obj = OTPRecords.objects.get(id = id)
    obj.delete()
    return HttpResponseRedirect(reverse('customers:otprecords'))

def customer_details(request):
    addresses = CustomerAddress.objects.all()
    if request.method == "POST":
        form = CustomerAddressForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auto_id = get_auto_id(CustomerAddress)
            instance.creator = request.user
            instance.updater = request.user
            instance.save()
            form = CustomerAddressForm()
            message = "Address added to db"
        else:
            message = generate_form_errors(form)
    else:
        form = CustomerAddressForm()
        message = False
    context = {
        'form': form,
        'addresses': addresses, 
        'title': 'Address List',
        'message': message,
    }
    return render( request, 'admin_panel/customers/customer-address/customer_address.html', context = context)


def delete_customer_details(request, id):
    obj = CustomerAddress.objects.get(id=id)
    obj.delete()

    return HttpResponseRedirect(reverse('customers:customer_details'))

def edit_customer_details(request, id):
    instance = get_object_or_404(CustomerAddress, id=id)
    if request.method == 'POST':
        form = CustomerAddressForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.updater = request.user
            instance.date_updated = datetime.now()
            instance.save()
            message = "Address updated"
        else:
            message = generate_form_errors(form)
    else:
        form = CustomerAddressForm(instance=instance)
        message = False
    context ={
        'form': form,
        'title': 'Address Editing Form',
        'message': message,
        'id':id,
    }
    return render(request, 'admin_panel/customers/customer-address/cutomer_address_edit.html', context = context)

#Quote Request#
def quote_requests(request):
    quote_requests = QuoteRequest.objects.all()

    if (quote_requests):
        context = {
            'quote_requests': quote_requests,
            'page_title':'Quote Requests | EQ-Bay',
            'message': False,
        }
        return render(request, 'admin_panel/customers/quoterequests/quote_request.html', context=context)
    else:
        context = {
            'page_title':'Quote Request | EQ-Bay',
            'message':'Quote List',
        }
        return render(request, 'admin_panel/nodata.html', context=context)

def create_quote_request(request):
    quote_requests = QuoteRequest.objects.all()
    if request.method == "POST":
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auto_id = get_auto_id(QuoteRequest)
            instance.creator = request.user
            instance.updater = request.user
            instance.save()
            form = QuoteRequestForm()
            message = "Request Sent Successfully"
        else:
            message = generate_form_errors(form)
    else:
        form = QuoteRequestForm()
        message = False
    context = {
        'form': form,
        'quote_requests': quote_requests, 
        'title': 'Quote Request List',
        'message': message,
    }
    return render(request, 'admin_panel/customers/quoterequests/quote_request.html', context = context)
    
def quote_request_view(request, id):
    data = QuoteRequest.objects.get(id=id)
    context = {
        'page_title':'Quote',
        'data':data,
    }
    return render(request, 'admin_panel/customers/quoterequests/quote_request_view.html', context=context)

def delete_quote(request, id):
    obj = get_object_or_404(QuoteRequest, id=id)
    obj.delete()

    response_data = {
        "title":"Successfully Deleted",
        "message":"Quote Request Deleted Successfully",
        "status":"success",
        "redirect":True,
        "redirect_url":reverse('dashboard:quote_requests'),
    }
    return HttpResponse(json.dumps(response_data),content_type="application/json")

def edit_quote(request, id):
    instance = get_object_or_404(QuoteRequest, id=id)
    if request.method == "POST":
        form = QuoteRequestForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.updater = request.user
            instance.date_updated = datetime.now()
            instance.save()
            message = "Quote updated successfully"
        else:
            message = generate_form_errors(form)
    else:
        form = QuoteRequestForm(instance=instance)
        message = False
    context = {
        'form': form,
        'title': 'Quote Request Edit',
        'message': message,
        'id': id,
    }
    return render(request, 'admin_panel/customers/quoterequests/quote_request_edit.html', context = context)


def quote_item_requests(request):
    quote_item_requests = QuoteRequestItem.objects.all()
    if request.method == "POST":
        form = QuoteRequestItemForm(request.POST)
        if form.is_valid():
            form.save()
            form = QuoteRequestItemForm()
            message = "Request submitted"
        else:
            message = generate_form_errors(form)
    else:
        form = QuoteRequestItemForm()
        message = False
    context = {
        'form': form,
        'quote_item_requests': quote_item_requests, 
        'title': 'Quote Item Request List',
        'message': message,
    }
    return render(request, 'admin_panel/customers/quote-request-item/quote_request_item.html', context = context)

class QuoteRequestAutoComplete(autocomplete.Select2QuerySetView):
   def get_queryset(self):
       if not self.request.user.is_authenticated:
           return QuoteRequest.objects.none()

       items = QuoteRequest.objects.all()

       if self.q:
           items = items.filter(Q(auto_id__istartswith=self.q) | Q(name__istartswith=self.q))

       return items

def delete_quote_item_request(request, id):
    obj = get_object_or_404(QuoteRequestItem, id=id)
    obj.delete()

    return HttpResponseRedirect(reverse('customers:quote_item_requests'))

def edit_quote_item_request(request, id):
    instance = get_object_or_404(QuoteRequestItem, id=id)
    if request.method == "POST":
        form = QuoteRequestItemForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            message = "Quote Item Request updated successfully"
        else:
            message = generate_form_errors(form)
    else:
        form = QuoteRequestItemForm(instance=instance)
        message = False
    context = {
        'form': form,
        'title': 'Quote Item Request Edit',
        'message': message,
        'id': id,
    }
    return render(request, 'admin_panel/customers/quote-request-item/quote_request_item_edit.html', context = context)


def rfqlist(request):
    rfq_list = RfqList.objects.all()
    if request.method == "POST":
        form = RfqListForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auto_id = get_auto_id(RfqList)
            instance.creator = request.user
            instance.updater = request.user
            instance.save()
            form = RfqListForm()
            message = "Rfq added"
        else:
            message = generate_form_errors(form)
    else:
        form = RfqListForm()
        message = False
    context = {
        'form': form,
        'title': 'Rfq List',
        'message': message,
        'rfqlist':rfq_list,
    }
    return render(request, 'admin_panel/customers/rfqlist/rfqlist.html', context = context)


def delete_rfq(request, id):
    obj = get_object_or_404(RfqList, id=id)
    obj.delete()

    return HttpResponseRedirect(reverse('customers:rfqlist'))


def edit_rfq(request, id):
    instance = get_object_or_404(RfqList, id=id)
    if request.method == "POST":
        form = RfqListForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.updater = request.user
            instance.date_updated = datetime.now()
            instance.save()
            message = "Rfq updated successfully"
        else:
            message = generate_form_errors(form)
    else:
        form = RfqListForm(instance=instance)
        message = False
    context = {
        'form': form,
        'title': 'Rfq List Edit',
        'message': message,
        'id': id,
    }
    return render(request, 'admin_panel/customers/rfqlist/rfqlist_edit.html', context = context)

