from django.db import models

# Create your models here.
class People(models.Model):
	name = models.CharField(max_length=100)
	birthday = models.DateField()
	sexial = models.CharField(max_length=1)
	university = models.CharField(max_length=100)
	department = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Introduction(models.Model):
	name = models.ForeignKey(People, on_delete=models.CASCADE)
	intro_context = models.CharField(max_length=255)
	
	
