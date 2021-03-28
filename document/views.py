from django.shortcuts import render, redirect
from .forms import CreateUserForm 
from .forms import ContactForm 
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#from .forms import OrderForm
#from .filters import OrderFilter
# Create your views here.
def l404(request):
    return render(request, 'l404.html')

def register(request):
        
    form = CreateUserForm()
    if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Votre compte a été créé '+ user)

                return redirect('loginPage')

    context={'form':form}
    return render(request, 'account/register.html', context) 

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  
            return redirect('lesenregistres') 
        else:
            messages.info(request, 'Username, password est incorrect')
    context={}
    return render(request, 'account/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('loginPage') 


def index(request):
    return render(request, 'index.html') 
#@login_required(redirect_field_name='loginPage')
@login_required(login_url='loginPage')
def patientformPage(request):
    #hopitals = Hopital.objects.all()
    form = ContactForm()
    context={'form':form}
    message= ""
    error=""
    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            #ENREGISTRER ET AFFICHER EN FONCTION DE L'ID
            form=form.save(commit=False) 
            form.user=request.user
            form.save()
            ##
            message="Inscription validée ."
            return redirect('lesenregistres')
        else:
            print(form.errors) 
            error="ok"
            form = ContactForm() 
    
    context={
        'form':form,
        'message':message,
        'error':error,
        #'hopitals' :hopitals,
        }
    return render(request, 'patientformPage.html' ,context)

@login_required(login_url='loginPage')
def lesenregistres(request):
    
    contacts = Contact.objects.filter(user= request.user); #ENREGISTRER ET AFFICHER EN FONCTION DE L'ID
    data = {}
    data['contacts'] = contacts
    return render(request, 'lesenregistres.html' , data)


@login_required(login_url='loginPage')
def details(request ,contact_id):
    id= int(contact_id)
    contact = Contact.objects.get(id=contact_id)
    form = ContactForm(data=(request.POST or None),files=(request.FILES or None),instance=contact,)
    if form.is_valid(): 
        form.save(commit=True) 
        return redirect('lesenregistres')

    context={
        'contact':contact,
        'form': form,
        }
    return render(request, 'details.html',context)

@login_required(login_url='account/login')
def modification(request ,contact_id):
    id= int(contact_id)
    contact = Contact.objects.get(id=contact_id)
    form = ContactForm(data=(request.POST or None),instance=contact,)
    if form.is_valid(): 
        form.save(commit=True) 
        return redirect('lesenregistres')

    context={
        'contact':contact,
        'form': form,
        }
    return render(request, 'modification.html',context)


def rechercheform(request):
    message = ""
    query = request.GET.get('query')
    if not query:
        contacts = Contact.objects.filter(user= request.user) # afficher tout en fonction des utilisateur 
    else:
        contacts = Contact.objects.filter(id__icontains=query)
        if not contacts.exists():
            contacts = Contact.objects.filter(diagnostique__icontains=query)
        if not contacts.exists():
            contacts = Contact.objects.filter(examen__icontains=query)
        if not contacts.exists():
            contacts = Contact.objects.filter(hopital__icontains=query)

        if not contacts.exists() :
            message ="Aucun resulat trouvé pour %s"%query
            context = {
                'message':message,
                }

    context = {
        'contacts':contacts,
        'message':message,
    }
    return render(request, 'lesenregistres.html', context)