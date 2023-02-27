from django.shortcuts import render
from shop.models import *
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
        'productData':productData
    }
   
    return render(r, "home.html",data)

def categoryWise(r, slug):
    categoryData=Category.objects.all()
    productData=Product.objects.filter(category__slug=slug)

    data={
        'categoryData':categoryData,
        'productData':productData
    }
    return render(r, "home.html",data)