from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime as dt
# Create your views here.


def homepage(request):
    t = dt.datetime.now()
    ht1 = "<html><head><meta http-equiv='refresh' content=10></head>"
    ht2 = f"<body><h1>{t}</h1></body></html>"
    return HttpResponse(ht1+ht2)

def index(request):
    return HttpResponse("<h1>Hello</h1>")

def number(requset,num):
    return HttpResponse(num)

def home(request):
    return render(request, 'home.html')

def info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = (name,email,password)
        return render(request,'info.html', {'d':data})
    return render(request, 'info.html')

def table(request,num):
    return render(request,'table.html',{'n':num,'range':range(1,11)})