from django.urls import path
from django.views.generic import TemplateView
from genealogy import views
#from django.views.generic import TemplateView

urlpatterns = [
    path('gene', views.gene, name='gene'),
    path('addmembers', views.addmembers, name='addmembers'),
    path('nodes', views.nodes, name='nodes'),
    #ppath('discute', views.discute, name='discute'),
    #path('register', views.register, name='register'),
    #path('logout', views.logout, name='logout'),
    #path('dashboard', views.dashboard, name='dashboard'),
    ]

