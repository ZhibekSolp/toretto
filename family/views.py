from re import template
from django.http import request
from django.shortcuts import render
from .models import Brain, Game

def main(request):
    brain=Brain.objects.all()
    context = {
        'brain': brain,

    }
    return render(request, template_name='family/index.html', context=context)

def supergame(request):
    game=Game.objects.all()
    contet = {
        'game': game,
    }
    return render(request, template_name='family/fast.html', context=contet)