from django.conf.urls import url
from . import views

urlpatterns = (
	url(r'^$', views.excercise_list, name='excercise_list'),
	)