from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index/index.html')

def Clinica(request):
    return render(request,'main/clinica1.html')

def login(request):
    return render(request,'login.html')