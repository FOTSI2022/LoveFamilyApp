from django.urls import path
from django.views.generic import TemplateView
from discussion import views
#from django.views.generic import TemplateView

urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('discute', views.discute, name='discute'),
    #path('create_theme_discussion', views.create_theme_discussion, name='create_theme_discussion'),
    #path('logout', views.logout, name='logout'),
    #path('dashboard', views.dashboard, name='dashboard'),
    ]

