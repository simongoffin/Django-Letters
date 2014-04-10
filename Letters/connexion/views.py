#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import redirect
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from connexion.forms import ConnexionForm
from connexion.forms import ProfilForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout                                                                  
from django.shortcuts import render                                                                     
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from game.forms import LettersForm

def creation(request):
    sauvegarde = False
    error=False
    if request.method == "POST":
        form = ProfilForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(nom, email,password)
            try:
                user.save()
                sauvegarde = True
                userT = authenticate(username=nom, password=password)
                if userT:  # Si l'objet renvoyé n'est pas None
                    login(request, userT)  # nous connectons l'utilisateur
                    form = LettersForm()  # Nous créons un formulaire vide
                    return render(request, 'game/home.html',locals())
                else: #sinon une erreur sera affichée
                    error = True
            except:
                error=True
    else:
        form = ProfilForm()
    return render(request, 'connexion/creation.html',locals())
    
def connexion(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]  # Nous récupérons le nom d'utilisateur
            password = form.cleaned_data["password"]  # … et le mot de passe
            user = authenticate(username=username, password=password)  #Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                form = LettersForm()  # Nous créons un formulaire vide
                return render(request, 'game/home.html',locals())
            else: #sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'connexion/connexion.html',locals())
    
def deconnexion(request):                                                                               
    logout(request)                                                                                     
    return redirect(reverse(connexion))
    
@login_required(login_url='/connexion/connexion/')
def confirmation(request):
    return render(request, 'connexion/confirmation.html')

