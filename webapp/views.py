from django.shortcuts import render
from .models import Etudiant,Cour
# Create your views here.

from django.http import HttpResponse
def home(request):
    #recupere
    etudiant = Etudiant.objects.all()
    cours = Cour.objects.all()
    context = {'cours': cours,'etudiants': etudiant}
   
    return render(request, 'webapp/fichier.html', context)
   