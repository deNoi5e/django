from django.shortcuts import render, get_object_or_404
from .models import Excercise
from django.utils import timezone

def excercise(request):
	excercises = get_object_or_404(Excercise)
	return render(request, 'fito/excercise_list.html', {'excercise': excercises})
