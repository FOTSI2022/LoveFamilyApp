from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
#from django.contrib import auth , login
from django.contrib import auth
from .models import *
from .forms import *
from django.views import generic
from accounts.choices import *


#from django.contrib.auth import logout

# Create your views here.
def register(request):
    g=['male', 'female']
    if request.method=="POST":
        #get form values
        last_name=request.POST['last_name']
        first_name=request.POST['first_name']
        username=request.POST['username']
        father=request.POST['father']
        mother=request.POST['mother']
        email=request.POST['email']
        gender=request.POST['gender']

        password=request.POST['password']
        password2=request.POST['password2']

         #check if passwords match
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                user=User(
                        last_name=last_name,
                        first_name=first_name,
                        username=username,                                            
                    )
                #ces deux lignes permettent de hasher le password et ssve le user
                user.set_password(password)
                user.save()

              
                #on verifie la présence du père dans le système ou non    
                fatherList = father.split(' ')
                fatherUser = User.objects.filter(first_name=fatherList[1], last_name=fatherList[0]).first()#first permet de recuperer l objet 
                if fatherUser is None:
                    fatherUser=User(first_name=fatherList[1], last_name=fatherList[0], username=fatherList[1]+'pere')
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
                        gender=gender,
                        email=email)
                    
                messages.success(request,'Vous êtes enregistré')
                return redirect('login')
        else:
             messages.error(request, 'Les paramètres renseignés ne sont pas corrects')
             return redirect('register')
    else:
        return render(request, 'accounts/register.html', {'g':g})


def login(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username, password=password )
        # user=authenticate(username=username, password=password )
        if user is not None:
            auth.login(request, user)
            #login(request, user)
            messages.success(request,'Vous êtes maintenant connecté!')
            return redirect('index')
        else:
            messages.error(request, 'Paraamètres non valides, essayez encore!')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def update_profile(request):
    g=['male', 'female']
    if request.method=="POST":
        
        #get form values
        if request.POST['phone_number']:
                phone_number=request.POST['phone_number']
        
        if request.POST['occupation']:
                occupation=request.POST['occupation']
        
        if request.POST['father_last_name']:
                father_last_name=request.POST['father_last_name']
        
        if request.POST['father_first_name']:
                father_first_name=request.POST['father_first_name']
        
        if request.POST['mother_last_name']:
                mother_last_name=request.POST['mother_last_name']
        
        if request.POST['mother_first_name']:
                mother_first_name=request.POST['mother_first_name']
        
        if request.POST['birth_country']:
                birth_country=request.POST['birth_country']
        
        if request.POST['birth_region']:
                birth_region=request.POST['birth_region']
       
        if request.POST['history']:
                history=request.POST['history']
        
        if request.POST.get('gender') :
                gender=request.POST['gender']
        
        if request.FILES.get('profile_image'):
                profile_image=request.FILES['profile_image']
        
        if request.POST['birth_date']:
                birth_date=request.POST['birth_date']

        p=''       
        #p= Person.objects.get(id= current_user.id) forbidden
        #if Person.objects.get(user= request.user):
        try:
            p= Person.objects.get(user= request.user)
        except:
            print('Personne non connectée')
        if Person.objects.get(user= request.user):
            p= Person.objects.get(user= request.user)
            if request.POST['birth_date']:
                p.birth_date=request.POST['birth_date']

            if request.POST['phone_number']:
                p.phone_number=request.POST['phone_number']
            
            if request.POST['occupation']:
                p.occupation=request.POST['occupation']
            
            if request.POST['birth_country']:
                p.birth_country=request.POST['birth_country']
            
            if request.POST['birth_region']:
                p.birth_region=request.POST['birth_region']
            
            if request.POST['history']:
                p.history=request.POST['history']
            
            if request.POST['father_last_name']:
                p.father_last_name=request.POST['father_last_name']
        
            if request.POST['father_first_name']:
                p.father_first_name=request.POST['father_first_name']
        
            if request.POST['mother_last_name']:
                    p.mother_last_name=request.POST['mother_last_name']
        
            if request.POST['mother_first_name']:
                    p.mother_first_name=request.POST['mother_first_name']
            
            if request.POST.get('gender') :
                p.gender=request.POST['gender']
           
            if request.FILES.get('profile_image'):
                p.profile_image=request.FILES['profile_image']
            
            p.personallyregister=False

            try:
                fatherUser=User.objects.filter(first_name=father_first_name, last_name=father_last_name)
            except:
                print("Le nom du père n'est pas enregistré")
            
            if fatherUser is None:
                fatherUser=User.objects.create(first_name=father_first_name, last_name=father_last_name, username=father_last_name+'pere')
                fatherUser.set_password('0000')
                fatherUser.save()

            try:
                motherUser=User.objects.filter(first_name=mother_first_name, last_name=mother_last_name)
            except:
                print("Le nom de la mère n'est pas enregistré")
            
            if motherUser is None:
                motherUser=User.objects.create(first_name=mother_first_name, last_name=mother_last_name, username=mother_last_name+'mere')
                motherUser.set_password('0000')
                motherUser.save()
                     
            p.save()

            messages.success(request,'vos informations ont été mises à jour')
            return redirect('index')
        else:
         
            p= Person.objects.create(
                        user=request.user,                                                         
                        father=fatherUser,
                        mother=motherUser,
                        gender=gender,
                        birth_date=birth_date,
                        phone_number=phone_number,
                        occupation=occupation,
                        birth_country=birth_country,
                        birth_region=birth_region,
                        history=history,
                        profile_image=profile_image     
        
                        )
             
                
        messages.success(request,'vos informations sont créées')
        return redirect('index')
    else:
        messages.error(request, "Une erreur s'est produite")
        return render(request, 'accounts/update_profile.html',{'g':g})


def profile(request):

    this_person= Person.objects.filter(user = request.user).first()
    
    context={'person':this_person,
                           }
     
    return render(request, 'accounts/profile.html', context)

def dashboard(request):
    #user_contacts =contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    #context={'contacts': user_contacts}
    return render(request, 'accounts/dashboard.html')

def logout(request):
    auth.logout(request)
    messages.success(request,'You are now loggout in!')
    return redirect('index')

    



