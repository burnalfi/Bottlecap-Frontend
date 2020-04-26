from django.urls import path
from main import views

urlpatterns = [
    path('', views.login, name='main-login'),
    path('home/', views.home, name='main-home'),
    path('login/', views.login, name='main-login'),
    path('logout/', views.logout, name='main-logout'),
    path('order/', views.order, name='main-order'),
    path('orders/', views.orders, name='main-orders'),
    path('parse/', views.parse, name='main-parse'),
    path('register/', views.register, name='main-register'),
    path('register/personal/', views.register_personal, name='main-regpersonal'),
    path('register/organization/', views.register_organization, name='main-regorganization'),
    

]