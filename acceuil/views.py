from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def acceuil_page(request):
    return render(request, "accueil.html")

def connexion_page(request):
    return render(request, "connexion.html")


