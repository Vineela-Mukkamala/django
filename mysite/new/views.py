from django.shortcuts import render
from django.template import loader


# Create your views here.
def index(request):
    return render(request,"index.html")

def name(request):
    
    return render(request,"indexname.html")
   

def interval(request):
    
    return render(request,"indexinterval.html")

def button(request):
    
    return render(request,"indexbutton.html")