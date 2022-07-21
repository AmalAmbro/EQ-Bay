from django.urls import path, re_path

from web.views import index

app_name = 'eqbay'

urlpatterns = [
    path('', index,name='index'),    
]
