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
        try:
            Messages.objects.create(content_message=text_comment, user=request.user.person)
        except:
            print("Messages non créés")
        
    family = []
    commentaires =[]

    #personne connectée
    this_person=Person.objects.filter(user=request.user).first() # ou bien user_id=request.user.id
    family.append(this_person)

    #pere de la personne connectée 
    father=""
    try:
        father=Person.objects.filter(user=this_person.father).first() # ou bien user_id=request.user.id
    except:
        print("Information sur le pere non renseignees")
    
    if father:
        family.append(father)

    #mere de la personne connectée
    mother="" 
    try:
        mother=Person.objects.filter(user=this_person.mother).first() # ou bien user_id=request.user.id
    except:
        print("Information sur la mere non renseignees")
    
    if mother:
        family.append(mother)
    
    #frere meme mère et père de la personne connectée
    brothers=""
    try:
        brothers= Person.objects.filter(mother=this_person.mother, father=this_person.father).exclude(user=request.user)
    except:
        print("Information sur les freres non renseignees")
    
    if brothers:
        family.append(brothers)
        
    for bro in brothers:
        family.append(bro) #enregistre tous les messages des frères

    #enfants de la personne connectée
    children=[]
    partner=""
    try:
        this_person.gender=="male"
        
        if this_person.gender=="male":
            try:
                children=Person.objects.filter(father_id=this_person.user_id)
            except:
                print("Informations non fournies sur les enfants de la personne connectée")
            
            if children:
                partner= children[0].mother
                for child in children:
                    family.append(child) #affiche tous les messages des enfants
                family.append(partner)
        else:
            try:
                children=Person.objects.filter(mother_id=this_person.user_id)
            except:
                print("Informations non fournies sur les enfants de la personne connectée")
            
            if children:
                partner= children[0].father
                for child in children:
                    family.append(child) #affiche tous les messages des enfants
                family.append(partner)
    
           
    except:
        print("Informations sur le sexe non fournie")
  

    for msg in Messages.objects.order_by('date_message'):
        if msg in commentaires:
                continue
        else:
            for member in family:
            
                if msg.user == member:
                    commentaires.append(msg)    

    return  render(request, 'discussion/discute.html', {'commentaires':commentaires})
