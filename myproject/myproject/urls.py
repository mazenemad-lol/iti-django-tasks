from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

admin.site.site_header = "لوحة تحكم إدارة النظام | Admin Dashboard"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "إدارة البيانات والتطبيقات (Articles, Tasks, Contacts)"

urlpatterns = [
    path('', lambda request: redirect('app1:home')),
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),
    path('app2/', include('app2.urls')),
    path('app3/', include('app3.urls')),
]
