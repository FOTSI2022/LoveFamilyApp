from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.models import *
#import graphviz

# Create your views here.
def gene(request):
    return  render(request, 'genealogy/gene.html')


def nodes(request):
     # recupere les données de la BDB à afficher dans un premier temps.
    #this_person=Person.objects.filter(user_id=request.user.id).first()
    this_person=Person.objects.filter(user=request.user).first() # ou bien user_id=request.user.id
    
    #frere meme mère et père de la personne connectée
    brothers= Person.objects.filter(mother=this_person.mother, father=this_person.father) 
    
    #frere meme mère de la personne connectée
    brothers_mother= Person.objects.filter(mother=this_person.mother) 
    
    #frere meme père de la personne connectée
    brothers_father= Person.objects.filter(father=this_person.father) 
    
    #enfants de la personne connectée
    children=Person.objects.filter(father_id=this_person.user_id) 
    
    #partner de la personne connectée
    
    partner= children[0].mother

    print(type(partner))
    print(partner.username)

    #les petits enfants de la personne connectée
    person = Person.objects.all()
    children_children=[]
    
    for child in children:
        for pers in person:
            if pers.father_id == child.user.id:
                children_children.append(pers)
    
    context={'person':this_person,
             'brothers':brothers,
             'children': children,
             'brothers_mother': brothers_mother,
             'brothers_father': brothers_father,
             'children_children': children_children,
             'partner': partner,
              }

    return  render(request, 'genealogy/nodes.html', context)

def addmembers(request):
    # recupere les données de la BDB à afficher dans un premier temps.
    #this_person=Person.objects.filter(user_id=request.user.id).first()
    this_person=Person.objects.filter(user=request.user).first() # ou bien user_id=request.user.id
    #all_person=Person.objects.all()
    brothers= Person.objects.filter(mother=this_person.mother, father=this_person.father) #frere meme mère et père
    #brothers_mother= Person.objects.filter(mother=this_person.mother) #frere meme mère 
    #brothers_father= Person.objects.filter(father=this_person.father) #frere meme père 
    #children=Person.objects.filter(father_id=this_person.user_id) #enfants
    """
    person = Person.objects.all()
    children_children=[]
    
    for child in children:
        for pers in person:
            if pers.father_id == child.user.id:
                children_children.append(pers)
    """
    context={'person':this_person,
             'brothers':brothers,
              }
        
    return  render(request, 'genealogy/addmembers.html', context) 