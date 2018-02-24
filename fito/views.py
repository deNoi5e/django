from django.shortcuts import render, get_object_or_404
from .models import Excercise
from django.utils import timezone


def excercise(request):
    excercises = get_object_or_404(Excercise)
    link_url = 'fito/excercise_list.html'
    return render(request, link_url, {'excercise': excercises})
