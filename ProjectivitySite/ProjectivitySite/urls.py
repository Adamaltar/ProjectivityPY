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
from . import settings
from django.conf.urls.static import static
from ProjectivityApp.views import get_notifications

# app_name = 'ProjectivityApp'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/users/', views.get_users, name='get_users'),
    path('', views.LoginView, name='login'),
    path('login/', views.LoginView, name='login'),
    path('login.html', views.LoginView, name='login'),
    path('contact2.html', views.Contact2View, name='contact2'),
    path('contact2/', views.Contact2View, name='contact2'),
    path('home.html', views.HomeView, name='home'),
    path('home/', views.HomeView, name='home'),
    path('logout/', views.LogoutView, name='logout'),
    path('contact/', views.ContactView, name='contact'),
    # path('contact.html', views.ContactView, name='contact'),
    path('proiecte/', views.ProiectView, name='proiecte'),
    path('taskuri/', views.TaskView, name='taskuri'),
    path('sedinte/', views.SedintaView, name='sedinte'),
    # path('proiecte.html', views.ProiectView, name='proiecte'),
    # path('taskuri.html', views.TaskuriView, name='taskuri'),
    # path('sedinte.html', views.SedinteView, name='sedinte'),
    path('get_notifications/', get_notifications, name='get_notifications'),
    # path('chat.html', views.ChatView, name='chat'),
    # path('chat/', views.ChatView, name='chat'),
    # path('chat/<int:chat_id>/messages', views.get_chat_messages, name='get_chat_messages'),
    # path('chat/<int:chat_id>/add_member/<int:user_id>', views.add_chat_member, name='add_chat_member'),
    path('chat/messages', views.save_message_to_database),
    path('chat/save', views.save_chat_to_database),
    # path('chat/<str:chatTitle>/messages', views.get_chat_messages),
    path('chat/<int:codChat>', views.delete_chat_from_database),
    path('chat/<str:numeChat>', views.update_chat_in_database),
    path('chat/<int:codChat>/invite', views.invite_members_to_chat),
    # path('rapoarte.html', views.RapoarteView, name='rapoarte'),
    path('detalii_utilizator.html', views.Detalii_utilizatorView, name='detalii_utilizator'),
    # path('detalii_utilizator/', views.Detalii_utilizatorView, name='detalii_utilizator'),
    path('info_utile.html', views.Info_utileView, name='info_utile'),
    # path('info_utile/', views.Info_utileView, name='info_utile'),
]    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

