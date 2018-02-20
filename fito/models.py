from django.db import models
from django.utils import timezone

#Описание упр
class Exercise(models.Model):
	group = models.CharField(max_length=150)
	title = models.CharField(max_length=40)
	text = models.TextField()
	# anim = models.ImageField
#Прогрес
#class Progress(models.Model):