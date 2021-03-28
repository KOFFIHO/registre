from django.urls import path, include
from . import views 
from django.conf.urls import url
from django.conf.urls.static import static
from docteur import settings

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^details/(?P<contact_id>[0-9]+)$', views.details, name='details'),
    url(r'^modification/(?P<contact_id>[0-9]+)$', views.modification, name='modification'),
    url(r'^rechercheform/$',views.rechercheform,name='rechercheform'),
    path('lesenregistres', views.lesenregistres, name='lesenregistres'),
    path('l404', views.l404, name='l404'),
    path('patientformPage', views.patientformPage, name='patientformPage'),
    path('account/login/', views.loginPage, name='loginPage'),
    path('account/logout/', views.logoutUser, name='logout'),
    path('account/register/', views.register, name='registerPage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
