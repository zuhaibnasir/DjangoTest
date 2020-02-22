from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

# Create your views here.
def home(request):
    recipies = Recipe.objects.all()
    return render(request, 'index.html',{'recipies' : recipies})

def categories(request):
    recipies = Recipe.objects.all()
    return render(request, 'categories.html',{'recipies' : recipies})