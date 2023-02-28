from django.shortcuts import render,redirect
from shop.models import *
from .forms import *
from django.core.paginator import Paginator

def homepage(r):
    categoryData=Category.objects.all()
    productData=Product.objects.all()

    if r.method=='GET':
        product=r.GET.get('product_search')
        if product!=None:
           productData=Product.objects.filter(category__title__icontains=product)

    data={
        'categoryData':categoryData,
        'productData':productData,
    }
    return render(r, "home.html",data)

def registration(r):
    form=StudentForm(r.POST or None)
    if r.method=="POST":
        if form.is_valid():
            form.save()
            return redirect(homepage)
    return render(r,'registration.html',{'form':form})
    

def categoryWise(r, slug):
    categoryData=Category.objects.all()
    productData=Product.objects.filter(category__slug=slug)

    data={
        'categoryData':categoryData,
        'productData':productData
    }
    return render(r, "home.html",data)

def singleView(r,slug):
    categoryData=Category.objects.all()
    data={}
    data['category']=categoryData
    data['product']=Product.objects.get(slug=slug)
    return render(r,"singleView.html",data)