from django.shortcuts import render,redirect
from django.http import HttpResponse
from module.models import user
import os
# Create your views here.
def index(request):
    return render(request,"index.html")
def Signup(request):
    u=user()
    u.name=request.GET.get("name")
    u.email=request.GET.get("email")
    u.password=request.GET.get("password")
    u.gender=request.GET.get("gender")
    u.dob=str(request.GET.get("dob"))
    u.state=request.GET.get("state")
    u.district=request.GET.get("district")
    u.save()
    request.session["email"] = request.GET.get("email")
    res = redirect("welcome")
    return res
def welcome(request):
    return render(request,"welcome.html")
def Login(request):
    u=user.objects.filter(email=request.GET.get("email"),password=request.GET.get("password"))
    if u.exists()==True:
        request.session["email"]=request.GET.get("email")
        res=redirect("welcome")
        return res
    else:
        return render(request,"index.html",{"error":'Invalid email id or password'})
def cp(request):
    return render(request,"cp.html")
def pfy(request):
    return render(request,"pfy.html")
def district(request):
    return render(request,"district1.html")
def logout(request):
    return render(request,"index.html")
def videos(request):
    a = []
    for i in os.listdir("F:\\crop\\croppred\\croppred\\static\\Video"):
        a.append(i)
    return render(request, "videolist.html", {"vlst": a})
def vplay(request):
    return render(request,"vplay.html",{"vname":request.GET.get("vname")})