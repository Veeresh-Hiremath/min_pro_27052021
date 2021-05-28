from django.shortcuts import render

def base(request):
    return render(request,"base.html")

def home(request):
    name="BASAVESHWAR ENGINEERING COOLEGE"
    return render(request,"home.html",{"name":name})

def department(request):
    return render(request,"department.html")

def placement(request):
    return render(request,"placement.html")

def contact(request):
    return render(request,"contact.html")

# Create your views here.
