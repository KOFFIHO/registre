from django.forms import ModelForm
from .models import Contact
from django import forms


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['nom','prenoms','profession','domicile_malade','date_naissance','ethnie','année','age','rhesus','groupe_sang','lieu_naissance','adresse_parent','telephone','Nom_urgence','telephone_urgent','Admission','resume','date_entree','conclusion','date_sortie','diagnostique','examen']
        widgets = {
            'nom': TextInput(attrs={'placeholder':'Quel est votre nom ?','class':'form-control','id':"name", 'name':"name"}),
            'prenoms': TextInput(attrs={'placeholder':'Quel est votre prenoms ?','class':'form-control','id':"name", 'name':"name"}),
            'profession': TextInput(attrs={'placeholder':'Votre profession ?','class':'form-control' , 'name':"name",} ),
            'domicile_malade': TextInput(attrs={'placeholder':'domicile du malade ?','class':'form-control','id':"subject"}),
            'année': TextInput(attrs={'placeholder':'année ?','class':'form-control','id':"subject"}),
            'ethnie': TextInput(attrs={'placeholder':'ethne ?','class':'form-control','id':"subject"}),
            'date_naissance': TextInput(attrs={'placeholder':'Quelle est votre date de naissance ?','class':'form-control','id':"email",}),
            'age': TextInput(attrs={'placeholder':'age du malade ?','class':'form-control','id':"subject"}),
            'rhesus': TextInput(attrs={'placeholder':'rhesus du malade ?','class':'form-control','id':"subject"}),
            'groupe_sang': TextInput(attrs={'placeholder':'groupe sang ?','class':'form-control','id':"subject"}),
            'hopital': TextInput(attrs={'placeholder':' hopital ?','class':'form-control','id':"subject"}),
            'lieu_naissance': TextInput(attrs={'placeholder':' hopital ?','class':'form-control','id':"subject"}),
            'adresse_parent': TextInput(attrs={'placeholder':' hopital ?','class':'form-control','id':"subject"}),
            'Nom_urgence': TextInput(attrs={'placeholder':' hopital ?','class':'form-control','id':"subject"}),
            'telephone_urgent': TextInput(attrs={'placeholder':' hopital ?','class':'form-control','id':"subject"}),
            'Admission': TextInput(attrs={'placeholder':' hopital ?','class':'form-control','id':"subject"}),
            'resume': TextInput(attrs={'placeholder':' hopital ?','class':'form-control','id':"subject"}),
            'conclusion': TextInput(attrs={'placeholder':' hopital ?','class':'form-control','id':"subject"}),
            'date_entree': TextInput(attrs={'placeholder':' hopital ?','class':'form-control','id':"subject"}),
            'date_sortie': TextInput(attrs={'placeholder':' hopital ?','class':'form-control','id':"subject"}),
            'diagnostique': TextInput(attrs={'placeholder':' hopital ?','class':'form-control','id':"subject"}),
            'examen': TextInput(attrs={'placeholder':' hopital ?','class':'form-control','id':"subject"}),

        }
        
