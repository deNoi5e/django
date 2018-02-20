from django.db import models
from django.utils import timezone

#Пользователь
class Users(models.Model):
	nickname = models.CharField(max_length=19)
	first_name = models.CharField(max_length=19)
	last_name = models.CharField(max_length=19)

	def publish(self):
		self.save()
	def __str__(self):
		return self.nickname

#Описание упр
class Excercise(models.Model):
	group = models.CharField(max_length=150)
	title = models.CharField(max_length=40)
	text = models.TextField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.title
	# anim = models.ImageField

#Текущее упражнение
class Train(models.Model):
	excercise = models.CharField(max_length=150)
	repeat = models.IntegerField()
	reiteration = models.IntegerField()
	date_train = models.DateField()