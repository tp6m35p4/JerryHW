from django.shortcuts import render
from .models import People, Introduction
# Create your views here.

def index(request, id=1):

	people = People.objects.get(pk=1)
	intro = Introduction.objects.get(name=people.id)
	return render(request, "intro/index.html", {'people':people, 'intro':intro})


def introPage(request, id=1):
	people = People.objects.get(pk=1)
	intro = Introduction.objects.get(name=people.id)
	return render(request, "intro/intro.html", {'people':people, 'intro':intro})