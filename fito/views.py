from django.shortcuts import render
from .models import Exercise
from django.utils import timezone

def excercise_list(request):
	excercise = Exercise.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'fito/excercise_list.html', {'excercise':excercise})
