from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User

from main.functions import get_current_role

from customers.models import Customer, OTPRecords

import json


def role_required(roles):
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            current_role = get_current_role(request)
            if not current_role in roles:
                if request.is_ajax():
                    response_data = {
                        "status": "false",
                        "stable": "true",
                        "title": "Permission Denied",
                        "message": "You have no permission to do this action."
                    }
                    return HttpResponse(json.dumps(response_data), content_type='application/javascript')
                else:
                    context = {
                        "title": "Permission Denied"
                    }
                    return render(request, 'errors/403.html', context)

            return view_method(request, *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper


def ajax_required(function):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return render(request,'error/400.html',{})
        return function(request, *args, **kwargs)
    wrap.__doc__=function.__doc__
    wrap.__name__=function.__name__
    return wrap


def otp_required(function):
    def wrapper(request, *args, **kwargs):
        print("I'm inside the decorator")
        data = Customer.objects.get(user=request.user)
        print(data.phone)
        if OTPRecords.objects.filter(phone=data.phone, is_verified=False).exists():
            return render(request, 'errors/403.html')
        return function(request, *args, **kwargs)
    
    return wrapper