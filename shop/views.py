from django.shortcuts import render

# Create your views here.
def homepage(r):
    return render(r, "header.html")