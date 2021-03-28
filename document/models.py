from django.db import models
from django.contrib.auth.models import User #APPEL USER 

# Create your models here.
class Sexe(models.Model):
    nom = models.CharField(max_length=100 ,blank=True ,null=True)
    def __str__(self):
        return self.nom

#class Hopital(models.Model):
 #   nom = models.CharField(max_length=100, blank=True ,null=True)
#    tel1 = models.IntegerField(blank=True ,null=True)
#    tel2 = models.IntegerField(blank=True ,null=True)
#    adress = models.CharField(max_length=500 ,blank=True ,null=True)
#    def __str__(self):
#        return self.nom


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,default=1)
    nom = models.CharField(max_length=50)
    prenoms = models.CharField(max_length=500)
    hopital = models.CharField(max_length=500)
    profession = models.CharField(max_length=100 ,blank=True ,null=True,)
    domicile_malade = models.CharField(max_length=5000,blank=True ,null=True)
    sexe = models.CharField(max_length=50)
    date_naissance = models.CharField(max_length=50, default=0)
    lieu_naissance= models.CharField(max_length=100 ,blank=True ,null=True)
    adresse_parent = models.CharField(max_length=100 ,blank=True ,null=True)
    telephone = models.CharField(max_length=50 , default=0)
    Nom_urgence = models.CharField(max_length=500 ,blank=True ,null=True)
    telephone_urgent = models.CharField(max_length=50 , default=0)
    admission = models.CharField(max_length=50)
    age = models.CharField(max_length=50 , default=0)
    resume = models.TextField(blank=True ,null=True)
    conclusion = models.TextField( blank=True ,null=True)
    date_entree = models.CharField(max_length=50, default=0)
    date_sortie = models.CharField(max_length=50, default=0)
    diagnostique = models.TextField(blank=True ,null=True)
    examen = models.TextField(blank=True ,null=True)
    resultat_examen = models.FileField(upload_to='examen')
    année = models.CharField(max_length=100 ,blank=True ,null=True)
    ethnie = models.CharField(max_length=100 ,blank=True ,null=True)
    groupe_sang = models.CharField(max_length=50 ,blank=True ,null=True)
    rhesus = models.CharField(max_length=100 ,blank=True  ,null=True)
    
    
    def __str__(self):
        return self.nom
       
