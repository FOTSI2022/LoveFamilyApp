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
    
    if request.method == 'POST':
        text_comment=request.POST['comment_text']
        Messages.objects.create(content_message=text_comment, user=request.user.person)
        
    family = []
    commentaires =[]

    #personne connectée 
    this_person=Person.objects.filter(user=request.user).first() # ou bien user_id=request.user.id
    family.append(this_person)

    #pere de la personne connectée 
    father=Person.objects.filter(user=this_person.father).first() # ou bien user_id=request.user.id
    family.append(father)

    #mere de la personne connectée 
    mother=Person.objects.filter(user=this_person.mother).first() # ou bien user_id=request.user.id
    family.append(mother)
    
    #frere meme mère et père de la personne connectée
    brothers= Person.objects.filter(mother=this_person.mother, father=this_person.father).exclude(user=request.user)
    
    #enfants de la personne connectée
    children=Person.objects.filter(father_id=this_person.user_id) 
    
    for child in children:
        family.append(child) #affiche tous les messages des enfants
    print(family)
    print("-------------------")
    for bro in brothers:
        family.append(bro) #enregistre tous les messages des frères
    print(family)
    print("-------------------")
    #partner de la personne connectée
    partner= children[0].mother
    family.append(partner)
    print(family)
    print("-------------------")
    for msg in Messages.objects.order_by('date_message'):
        if msg in commentaires:
                continue
        else:
            for member in family:
            
                if msg.user == member:
                    commentaires.append(msg)    
    print(commentaires)
    return  render(request, 'discussion/discute.html', {'commentaires':commentaires})
