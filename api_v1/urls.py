from django.urls import path
from . import views

urlpatterns=[
    path('register', views.register_page, name='_register-view'),
    path('login', views.login_page, name='_login-view'),
    path('logout', views.logout_page, name='_logout-view'),
    path('submit', views.submit_page, name='_submit-view'),
    path('search', views.search_page, name="_search-view"),
]