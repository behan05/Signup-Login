from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('signup/', views.signup, name='Signup'),
    path('signin/', views.signin, name='Signin'),
]