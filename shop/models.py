from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    contact=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=200)
    dob=models.DateField()

class Category(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(null=True)
    slug=models.SlugField()

    def __str__(self):
        return self.title
        
class Product(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    description=models.TextField()
    image=models.ImageField()
    price=models.FloatField()
    slug=models.SlugField( null=True,blank=True)
    discount_price=models.FloatField(null=True,blank=True)
    brand=models.CharField(max_length=200)

    def __str__(self):
        return self.name