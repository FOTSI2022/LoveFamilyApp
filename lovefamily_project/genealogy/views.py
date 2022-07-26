from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import *
from django.views import generic
from django.contrib import messages
#import graphviz

# Create your views here.
def gene(request):
    return  render(request, 'genealogy/gene.html')


def nodes(request):
     # recupere les données de la BDB à afficher dans un premier temps.
    #this_person=Person.objects.filter(user_id=request.user.id).first()
    this_person=Person.objects.filter(user=request.user).first() # ou bien user_id=request.user.id
    
    #frere meme mère et père de la personne connectée
    brothers=''
    try:
        brothers=Person.objects.filter(mother=this_person.mother, father=this_person.father)
    except:
        print("Informations sur les frères non disponibles")
        
    #frere meme mère de la personne connectée
    brothers_mother=''
    try:
        brothers_mother= Person.objects.filter(mother=this_person.mother) 
    except:
        print("Informations sur les frères de même mère non disponibles")

        
    #frere meme père de la personne connectée
    brothers_father=''
    try:
        brothers_father= Person.objects.filter(father=this_person.father) 
    except:
        print("Informations sur les frères de même père non disponibles")


    #parents et grands parents  de la personne connectée
    #côté father
    father='' #père de la personne connectée
    grandmother='' #grand-père de la personne connectée coté paternel
    grandfather='' #grand-père de la personne connectée côté paternel
    try:
        father= this_person.father
    except:
        print("informations sur le père de la personne connectée non fournies")
    
    if father:
        try:
            grandfather= father.father
        except:
            print("Informations sur le grand père du père de la personne connectée non fournies")
        
        try:
            grandmother= father.mother
        except:
            print("Informations sur la grande mère du père de la personne connectée  non fournies")

   
    #côté mother
    mother='' #mère de la personne connectée
    grandmother_mother='' #grande mère de la personne connectée côté maternel
    grandfather_mother='' #grand-père de la personne connectée côté maternel
    try:
        mother= this_person.mother
    except:
        print("Informations sur la grand père de la mère de la personne connectée non fournie")
    
    if mother:
        try:
            grandfather_mother= mother.father
        except:
            print("Informations sur le grand père maternel de la personne connectée non fournies")
        
        try:
            grandmother_mother= mother.mother
        except:
            print("Informations sur la grande mère maternelle de la personne connectée non fournies ")
      
    
    
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
        else:
            try:
                children=Person.objects.filter(mother_id=this_person.user_id)
            except:
                print("Informations non fournies sur les enfants de la personne connectée")
            
            if children:
                partner= children[0].father
    except:
        ("Informations sur le sexe non fournie")
    

    
    #parents et grands parents du partenaire  de la personne connectée
    father_part='' #père  partner
    grandmother_part='' #grande-mère du partner côté paternel
    grandfather_part='' #grand-père du partner côté paternel
    try:
        father_part= partner.father
    except:
        print('Information sur le père du partner non fournie')

    if father_part:
        try:
            grandfather_part= father_part.father 
        except:
            print("Information sur la mêre du père du partner non fournie")
        
        try:
            grandmother_part= father_part.mother 
        except:
            print("Information sur la mêre du père partner non fournie")

    
    #côté mother du patenaire
    #côté mother
    mother_part='' #mère du partner 
    grandmother_part_mother='' #grande-mère du partner côté maternel
    grandfather_part_mother='' #grand-père du partner côté maternel
    
    try:
        mother_part= partner.mother
    except:
        print('Information sur la mère du partner non fournie')

    if mother_part:
        try:
            grandfather_part_mother= mother_part.father 
        except:
            print("Information sur la mêre de la mêre du partner non fournie")
        
        try:
            grandmother_part_mother= father_part.mother 
        except:
            print("Information sur la mêre du père partner non fournie")

    

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
             'father': father,
             'mother': mother,
             'grandmother': grandmother,
             'grandfather': grandfather,
             'grandmother_part': grandmother_part,
             'grandfather_part': grandfather_part,
             'grandmother_part_mother': grandmother_part_mother,
             'grandfather_part_mother': grandfather_part_mother,
             #'grandfather': grandfather,
              }

    return  render(request, 'genealogy/nodes.html', context)


def addmembers(request):
    g=['male', 'female']
    if request.method=="POST":
        #get form values
        last_name=request.POST['last_name']
        first_name=request.POST['first_name']
        username=last_name+first_name
        father=request.POST['father']
        mother=request.POST['mother']
        gender=request.POST['gender']

        user=User(
                last_name=last_name,
                first_name=first_name,
                username=username
                                                            
                )

        #ces deux lignes permettent de hasher le password et ssve le user
        user.set_password('0000')
        user.save()

              
        #on verifie la présence du père dans le système ou non    
        fatherList = father.split(' ')
        fatherUser = User.objects.filter(first_name=fatherList[1], last_name=fatherList[0]).first()#first permet de recuperer l objet 
        if fatherUser is None:
            fatherUser=User(first_name=fatherList[1], last_name=fatherList[0])
            fatherUser.set_password('0000')
            fatherUser.save()
                
        #on verifie la présence du père dans la mère dans le système ou non 
        motherList = mother.split(' ')
        motherUser = User.objects.filter(first_name=motherList[1], last_name=motherList[0]).first()#first permet de recuperer l objet 
        if motherUser is None:
            motherUser=User.objects.create(first_name=motherList[1], last_name=motherList[0], username=motherList[1]+'mere')
            motherUser.set_password('0000')
            motherUser.save()
                
        p= Person.objects.create(
                user=user,
                father=fatherUser,
                mother=motherUser,
                gender=gender)
                    
        messages.success(request,'Vous avez enregistré')
                
        return redirect('addmembers')
    else:
        return render(request, 'genealogy/addmembers.html', {'g':g})
