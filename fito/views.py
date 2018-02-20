from django.shortcuts import render
from .models import Excercise
from django.utils import timezone

def excercise(request):
	excercise = Excercise.objects.order_by('group')
	return render(request, 'fito/excercise_list.html', {'excercise':excercise})
