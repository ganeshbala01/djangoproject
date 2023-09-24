from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'first.html',{'profilelink':'http://127.0.0.1:8000/profile/'})

def secondpage(request):
    return render(request,'second.html',{'homelink':'http://127.0.0.1:8000/'})

def calculate(request):
    a=int(request.GET['text-box-1'])
    b=int(request.GET['text-box-2'])
    c=a+2*b
    return render(request,'output.html',{'result':c})