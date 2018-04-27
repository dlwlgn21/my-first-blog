
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'',include('blog.urls')),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
]
