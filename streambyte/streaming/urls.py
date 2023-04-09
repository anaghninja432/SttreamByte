from django.contrib import admin
from django.urls import path, include
from streaming import views 

admin.site.site_header = "StreamByte Admin"
admin.site.site_title = "StreamByte Portal"
admin.site.index_title = "Welcome to StreamByte Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('free', views.free, name='free'),
    path('paid',views.paid, name='paid'),
    path('forcreators', views.forcreators, name='forcreators'),
    path('contactus', views.contactus, name='contactus'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('handlelogin',views.handlelogin,name='handlelogin'),
    path('logout',views.logout,name='logout'),
]
