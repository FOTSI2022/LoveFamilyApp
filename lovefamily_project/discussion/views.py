from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.db import models
from django.http import HttpResponse


# Create your views here.

# Create your views here.

def index(request):
    
    return  render(request, 'home.html')

def about(request):
       
    return  render(request, 'about.html')

def discute(request):
    family = []
    commentaires =[]
    #create un message 
    this_person=Person.objects.filter(user=request.user).first() # ou bien user_id=request.user.id
    family.append(this_person)
    #frere meme mère et père de la personne connectée
    brothers= Person.objects.filter(mother=this_person.mother, father=this_person.father) 
     
    #enfants de la personne connectée
    children=Person.objects.filter(father_id=this_person.user_id) 

    for child in children:
        family.append(child) #affiche tous les messages

    for bro in brothers:
        family.append(bro) #affiche tous les messages

    for msg in Messages.objects.order_by('date_message'):
        for member in family:
            if msg.user == member:
                commentaires.append(msg)

    if request.method == 'POST':
        text_comment=request.POST['comment_text']
        Messages.objects.create(content_message=text_comment, user=request.user.person)             
      
    return  render(request, 'discussion/discute.html', {'commentaires':commentaires})

""""
def create_theme_discussion(request):
    form = AddThemeForm()
    if request.method == 'POST':
        form = AddThemeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('discute')
        else:
            messages.error(request, 'Thème de discussion non créé')
           
    return render(request, 'discussion/create_theme_discussion.html', {'form':form})

"""
