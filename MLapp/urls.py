from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home' ),
    path('prediction/',views.prediction,name='prediction'),
    path('loginUser/',views.loginUser,name='loginUser'),
    path('logoutUser/',views.logoutUser,name='logoutUser'),
    path('singupUser/',views.register_user,name='signupUser'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    
   
]