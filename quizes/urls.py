from django.urls import path
from . import views

urlpatterns=[
    path('', views.home_page, name='home-view'),
    path('register', views.register_page, name='register-view'),
    path('login', views.login_page, name='login-view'),
    path('logout', views.logout_page, name='logout-view'),
]