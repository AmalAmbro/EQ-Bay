from django.urls import path
from main.views import index, otpvalidation

app_name = 'main'

urlpatterns = [
    path('', index,name='index'),
    # path('home/', home,name='home'),
    path('otp/', otpvalidation, name='otp' ),
]
