from django.urls import path
from . import views

urlpatterns=[
    path("", views.acceuil_page),
    path("connexion/",views.connexion_page)
]