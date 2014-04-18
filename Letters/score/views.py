from django.shortcuts import render
from challenge.models import Score
# Create your views here.



def score(request):
    liste=Score.objects.order_by('-score','temps')
    l0='nom: '+liste[0].user_name+' score: '+str(liste[0].score)+' temps: '+str(liste[0].temps)+' sec'
    l1='nom: '+liste[1].user_name+' score: '+str(liste[1].score)+' temps: '+str(liste[1].temps)+' sec'
    l2='nom: '+liste[2].user_name+' score: '+str(liste[2].score)+' temps: '+str(liste[2].temps)+' sec'
    return render(request, 'score/score.html',locals())