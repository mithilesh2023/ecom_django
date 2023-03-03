from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from .forms import *

# from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from shop.forms import RegirationForm
from django.contrib.auth import authenticate,login as LoginFun,logout
from datetime import datetime
from django.contrib.auth.decorators import login_required

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

# -------regiration function start----------------------------
# def registration(r):
#     form=StudentForm(r.POST or None)
#     if r.method=="POST":
#         if form.is_valid():
#             form.save()
#             return redirect(homepage)
#     return render(r,'registration.html',{'form':form})

def registration(r):
    form=RegirationForm(r.POST or None)
    if r.method=='POST':
        if form.is_valid():
            form.save()
            return redirect(login)
    data={}
    data['form']=form
    return render(r, 'registration.html',data)
# -------regiration function end----------------------------
    

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
    LoginForm=AuthenticationForm(r.POST or None)
    if r.method=='POST':
            username=r.POST.get('username')
            password=r.POST.get('password')

            user=authenticate(username=username,password=password)
            if user is not None:
                LoginFun(r, user)
                return redirect(homepage)

    return render(r,'login.html',{'form':LoginForm})

# ----------------login function end------------------
# ----------------logout function start------------------

def logoutAuth(r):
    logout(r)
    return redirect(homepage)
# ----------------logout function end------------------

#-----------addToCart start ------------------------
@login_required()
def addToCart(r,slug):
    product=get_object_or_404(Product,slug=slug)

    order_item,created=OrderItem.objects.get_or_create(user=r.user,ordered=False,item=product)

    order_qs=Order.objects.filter(user=r.user,ordered=False)

    if order_qs.exists():
        order=order_qs[0]
        #order record already exist
        if (order.items.filter(item__slug=slug).exists()):
            order_item.qty += 1
            order_item.save()
        else:
            order.items.add(order_item)
            return redirect(homepage)
    else:
        #need to create new order record
        order=Order.objects.create(user=r.user)
        order.items.add(order_item)
        #msg:this item is added to your cart
        return redirect(homepage)

#-----------addToCart end ------------------------

  