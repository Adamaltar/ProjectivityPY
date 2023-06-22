"""
URL configuration for ProjectivitySite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ProjectivityApp import views

# app_name = 'ProjectivityApp'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.LoginView, name='login'),
    path('login/', views.LoginView, name='login'),
    path('login.html', views.LoginView, name='login'),
    path('contact2.html', views.Contact2View, name='contact2'),
    path('home.html', views.HomeView, name='home'),
    path('home/', views.HomeView, name='home'),
    path('logout/', views.LogoutView, name='logout'),
    path('contact/', views.ContactView, name='contact'),
    path('contact.html', views.ContactView, name='contact'),
    path('proiecte/', views.ProiectView, name='proiecte'),
    path('proiecte.html', views.ProiectView, name='proiecte'),
    # path('taskuri.html', views.TaskuriView, name='taskuri'),
    # path('sedinte.html', views.SedinteView, name='sedinte'),
    # path('chat.html', views.ChatView, name='chat'),
    # path('rapoarte.html', views.RapoarteView, name='rapoarte'),
    path('detalii_utilizator.html', views.Detalii_utilizatorView, name='detalii_utilizator'),
    path('detalii_utilizator/', views.Detalii_utilizatorView, name='detalii_utilizator'),
    path('info_utile.html', views.Info_utileView, name='info_utile'),
    path('info_utile/', views.Info_utileView, name='info_utile'),
    
    # path('', views.ProiectView, name='proiecte'),
    # path('login.html', views.LoginView, name='login'),
    # path('home.html', views.HomeView, name='home'),
    # path('proiecte.html', views.ProiectView, name='proiecte'),
    # path('registration/contact.html', name='contact'),
    # path('registration/contact2.html', name='contact2'),
    # path('registration/info_utile.html', name='info_utile'),
    # path('login/', views.LoginView, name='login'),
    # path('home/', views.HomeView, name='home'),
    # path('logout_view/', views.LogoutView, name='logout_view'),  
]

