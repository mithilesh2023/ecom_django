from django.shortcuts import render,redirect
from shop.models import *
from .forms import *
# from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login as LoginFun,logout
from datetime import datetime

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

# ----------------login function start------------------
def login(r):
    LoginForm=AuthenticationForm(r,data=r.POST or None)
    if r.method=='POST':
        if LoginForm.is_valid():
            username=LoginForm.cleaned_data.get('username')
            password=LoginForm.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                print(user)
                LoginFun(r, user)
                return redirect(homepage)
            else:
                return redirect(login)
    return render(r,'login.html',{'form':LoginForm})

def logoutFunction(r):
    logout(r)
    return redirect(login)

# ----------------login function end------------------
