from django.contrib import admin
from django.views.static import serve
from django.urls import include, path, re_path
from eqbay import settings
from main import views as general_views

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('eqbay-admin/', admin.site.urls),
    path('app/',include(('main.urls'),namespace='main')),   
    path('category/',include(('products.urls'),namespace='category')), 
    path('customers/',include(('customers.urls'),namespace='customers')), 
    path('eqbay/',include(('web.urls'),namespace='eqbay')),   
    path('dashboard/',include(('dashboard.urls'),namespace='dashboard')),   
    path('app/',general_views.app,name='app'), 
    path('app/accounts/', include('registration.backends.default.urls')),
    
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]