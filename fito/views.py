from django.shortcuts import render
from .models import Excercise
from django.utils import timezone

def excercise(request):
	#excercise = Exercise.objects.filter(published_date_lte=timezone.now()).order_by('published_date')
	return render(request, 'fito/excercise_list.html', {'excercise':excercise})
