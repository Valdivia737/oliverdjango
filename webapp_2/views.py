from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def harry1(request):
    return render(request,'harry1.html')

def harry2(request):
    return render(request,'harry2.html')

def harry3(request):
    return render(request,'harry3.html')

def harry4(request):
    return render(request,'harry4.html')    

def harry5(request):
    return render(request,'harry5.html')

def harry6(request):
    return render(request,'harry6.html')




