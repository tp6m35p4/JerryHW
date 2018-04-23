from django.urls import path
from . import views

urlpatterns = [
	path('', views.introPage, name='index'),
	path('<int:id>', views.introPage, name='intro')

]