
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('user_login',views.ulogin,name='user_login'),
    path('register',views.register,name='register'),
]
