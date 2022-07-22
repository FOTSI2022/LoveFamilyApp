from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('profile', views.profile, name='profile'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    ]

