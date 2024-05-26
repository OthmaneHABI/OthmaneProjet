from django import views
from django.urls import path,include
from .views import*

urlpatterns = [
    path('',acceuil, name='acceuil'),
    path('',service, name='service'),
    path('',aboutus, name='aboutus'),
     path('register/', views.register_view, name='register'),
    path('login/', views.login_view,name='login'),

   
]
