from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.urls import reverse
import datetime
from main.decorators import otp_required
# from main.decorators import otp_required
from main.form import Userform
from main.functions import get_otp
from customers.models import Customer, OTPRecords


# @check_mode

@login_required
def app(request):
    return HttpResponseRedirect(reverse('index'))

# Create your views here.

# @role_required(['superadmin'])
@login_required
# @otp_required
def index(request):
    today = datetime.date.today() + datetime.timedelta(days=1)
    customers = Customer.objects.all()
    # data = Customer.objects.get(user=request.user)
    # instance = OTPRecords.objects.get(phone=data.phone)
    # instance.is_verified = False
    # instance.save()
    if request.user.is_superuser:
        context = {
            'page_title' : 'Dashboard',
            'customers': customers,
        }
        return render(request,'admin_panel/index.html', context)
    
    else:

        user = request.user

        context = {
            'page_title': 'EQ-Bay | Home',
        }
        return render(request, 'user_panel/home.html')


def otpvalidation(request):

    user = request.user
    message = ""
    data = Customer.objects.get(user = user)
    phone = data.phone

    if not OTPRecords.objects.filter(phone=phone).exists():
        OTPRecords.objects.create(
            phone = phone,
            otp = get_otp(),
            attempts = 0,
        )
    #code to provide random otp for respected numbers
    # else:
    #     instance = OTPRecords.objects.get(phone=phone)
    #     instance.otp = get_otp()
    #     instance.attempts = 0
    #     instance.save()\
            
    if request.method == "POST":
        if OTPRecords.objects.filter(phone=phone).exists():
            instance = get_object_or_404(OTPRecords, phone=phone)
            otp = instance.otp
            instance.attempts = instance.attempts + 1
            otp_got = request.POST.get('otp')
            if (otp_got == otp):
                print("Verified successfully")
                message = "Verified successfully"
                instance.is_verified = True
                instance.save()
                return HttpResponseRedirect(reverse('main:index'))
            else:
                message = "OTP mismatch"
            instance.save()
        else:
            message = "Phone not added"

        

    context = {
        'page_title': 'OTP Validation',
        'message': message,
        'phone': phone,
    }
    return render(request, 'otp/otp.html', context=context)