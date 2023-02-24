from django.shortcuts import render
from shop.models import *
# Create your views here.
def getCategory():
    return Category.objects.all()
def homepage(r):
    data={}
    data['category']=getCategory()
    return render(r, "home.html",data)