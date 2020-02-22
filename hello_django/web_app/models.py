from django.db import models

# Create your models here.
  
class Category(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()

class Recipe(models.Model):
    name=models.CharField(max_length=200)
    intro=models.CharField(max_length=400)
    description=models.TextField()
    img= models.ImageField(upload_to='images')
    price=models.FloatField()
    active=models.BooleanField(default=True)
    category = models.ManyToManyField(Category)