from django.shortcuts import render
from shop.models import *
# from .models import Product


# Create your views here.

# def getCategory():
#     return Category.objects.all()
    # data={
    #     'categoryData':catrgoryData
    # }
    # return render(r,'home.html',data)
def homepage(r):
    categoryData=Category.objects.all()
    productData=Product.objects.all()[:8]
    data={
        'categoryData':categoryData,
        'productData':productData
    }
    # categoryData:{}
    # categoryData['category']=getCategory()
    # data['category']=getCategory()
    return render(r, "home.html",data)