from django.contrib import admin


from .models import Sexe
from .models import Contact
#from .models import Hopital
# Register your models here.

class AdminContact(admin.ModelAdmin):
    list_display = ['nom']


class AdminSexe(admin.ModelAdmin): 
    list_display = ['nom']

#lass AdminHopital(admin.ModelAdmin): 
  #  list_display = ['nom']

admin.site.register(Sexe, AdminSexe)

admin.site.register(Contact, AdminContact)

#admin.site.register(Hopital, AdminHopital) 
