from django.forms import ModelForm, TextInput, EmailInput,Textarea,DateInput
from django.forms import ModelForm
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['nom','prenoms','sexe','resultat_examen','profession','domicile_malade','date_naissance','ethnie','année','age','rhesus','groupe_sang','lieu_naissance','adresse_parent','telephone','Nom_urgence','telephone_urgent','hopital','resume','date_entree','conclusion','date_sortie','diagnostique','examen','admission']
        
        widgets = {
            'nom': TextInput(attrs={'placeholder':'Nom du patient ?','class':'form-control','id':"name", 'name':"name"}),
            'prenoms': TextInput(attrs={'placeholder':'Prenoms du patient ?','class':'form-control','id':"name", 'name':"name"}),
            'profession': TextInput(attrs={'placeholder':'Profession du patient ?','class':'form-control' , 'name':"name",} ),
            'sexe': TextInput(attrs={'placeholder':'Sexe du patient ?','class':'form-control' , 'name':"name",} ),
            'domicile_malade': TextInput(attrs={'placeholder':'domicile du patient ?','class':'form-control','id':"subject"}),
            'année': TextInput(attrs={'placeholder':'année actuelle ?','class':'form-control','id':"subject"}),
            'ethnie': TextInput(attrs={'placeholder':'Ethnie  du pateint?','class':'form-control','id':"subject"}),
            'date_naissance': DateInput(attrs={'placeholder':'Date de naissance du patient?','class':'form-control','id':"email",}),
            'age': TextInput(attrs={'placeholder':'Âge du patient ?','class':'form-control','id':"subject"}),
            'telephone': TextInput(attrs={'placeholder':'Numéro du patient ?','class':'form-control','id':"subject"}),
            'rhesus': TextInput(attrs={'placeholder':'Rhesus du patent ?','class':'form-control','id':"subject"}),
            'groupe_sang': TextInput(attrs={'placeholder':'groupe sangin du patient ?','class':'form-control','id':"subject"}),
            'admission': TextInput(attrs={'placeholder':' Dans quel service est il admis ?','class':'form-control','id':"subject"}),
            'lieu_naissance': TextInput(attrs={'placeholder':' Lieu de naissance du patient ?','class':'form-control','id':"subject"}),
            'adresse_parent': TextInput(attrs={'placeholder':' Adresse des parents du patient ?','class':'form-control','id':"subject"}),
            'Nom_urgence': TextInput(attrs={'placeholder':' Nom (appeler en cas d\'urgence) ?','class':'form-control','id':"subject"}),
            'telephone_urgent': TextInput(attrs={'placeholder':' Numero d\'urgence ?','class':'form-control','id':"subject"}),
            'hopital': TextInput(attrs={'placeholder':' Nom de l\'hopital ?','class':'form-control','id':"subject"}),
            'resume': TextInput(attrs={'placeholder':' Résumé ?','class':'form-control','id':"subject"}),
            'conclusion': TextInput(attrs={'placeholder':' Conclusion ?','class':'form-control','id':"subject"}),
            'date_entree': DateInput(attrs={'placeholder':' Date d\'entrée d\'hopital?','class':'form-control','id':"subject"}),
            'date_sortie': DateInput(attrs={'placeholder':'  Date de sortie d\'hopital ?','class':'form-control','id':"subject"}),
            'diagnostique': TextInput(attrs={'placeholder':' DIAGNOSTIQUE ?','class':'form-control','id':"subject"}),
            'examen': TextInput(attrs={'placeholder':' Les differents examen demandés ?','class':'form-control','id':"subject"}),
        }
    
       