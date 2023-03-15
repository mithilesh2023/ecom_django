from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from .forms import *
from .forms import AddressForm
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

def checkout(r):
    form=AddressForm(r.POST or None)
    addresses=Address.objects.filter(user=r.user)
    if r.method=="POST":
        if form.is_valid():
            f=form.save(commit=False)
            f.user=r.user
            f.save()
            return redirect(checkout)

    return render(r, 'checkout.html',{"form":form,"addresses":addresses}) 

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
        return redirect(myCart)
    else:
        #need to create new order record
        order=Order.objects.create(user=r.user)
        order.items.add(order_item)
        #msg:this item is added to your cart
        return redirect(myCart)

#-----------addToCart end ------------------------
@login_required()
def myCart(r):
    data={}
    data['order']=Order.objects.get(user=r.user,ordered=False)
    return render(r, 'cart.html',data)

@login_required()
def removeFromCart(r,slug):
    product=get_object_or_404(Product,slug=slug)
    order=Order.objects.get(user=r.user,ordered=False)
    order_item=OrderItem.objects.get(user=r.user,ordered=False,item=product)
    if order:
        if(order.items.filter(item__slug=slug).exists()):
            if order_item.qty <=1:
                order_item.delete()
            else:
                order_item.qty-=1
                order_item.save()
        return redirect(myCart)

def checkCode(code):
    try:
        coupon =Coupon.objects.get(code=code)
        return True
    except:
        return False

def getCoupon(code):
    try:
        coupon=Coupon.objects.get(code=code)
        return coupon
    except:
        return redirect(myCart)

def addCoupon(r):
    code=r.POST.get('code')

    if checkCode(code):
        coupon = getCoupon(code)
        order=Order.objects.get(user=r.user,ordered=False)
        order.coupon=coupon
        order.save()
        #successfully coupon applied
    return redirect(myCart)

def removeCoupon(r):
    order=Order.objects.get(user=r.user,ordered=False)
    order.coupon=None
    order.save()
    return redirect(myCart)

def checkout(r):
    form =AddressForm(r.POST or None)
    addresses=Address.objects.filter(user=r.user)
    if r.method=='POST':
        if form.is_valid():
            f=form.save(commit=False)
            f.user=r.user
            f.save()

            order=Order.objects.get(user=r.user,ordered=False)
            order.address=f
            order.save()

            return redirect(checkout)
    return render(r, 'checkout.html',{"form":form,"addresses":addresses})

def checkoutWithSaveAddress(r):
    if r.method=='POST':
        address_id=r.POST.get('saved_address')
        address=Address.objects.get(pk=address_id)
        order=Order.objects.get(user=r.user,ordered=False)
        order.address=address
        order.save()
        return redirect(checkout)
    

  