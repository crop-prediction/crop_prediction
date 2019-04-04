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
def prediction(request):
    return render(request,"prediction.html")
def roh(request):
    x=int(request.GET.get("area"))
    nm=str(request.GET.get("crop"))
    print(nm)
    if nm == "Wheat":
        y=WheatPred(x)
    else:
        y=BajraPred(x)
    return render(request,"production.html",{"prod":y,"crop":nm,"area":x})
def WheatPred(x):
    print("h2")
    data=pd.read_csv('F:\crop\croppred\module\data1.csv')
    X=data['Production'].values
    Y=data['Area'].values
    mean_x = np.mean(X)
    mean_y = np.mean(Y)
    m = len(X)
    num = 0
    den = 0
    for i in range(m):
        num += (X[i] - mean_x) * (Y[i] - mean_y)
        den += (X[i] - mean_x) ** 2
    b1 = num / den
    b0 = mean_y - (b1* mean_x)
    y=b1*x
    return y
def BajraPred(x):
    print("h3")
    data=pd.read_csv('F:\crop\croppred\module\data2.csv')
    X=data['Production'].values
    Y=data['Area'].values
    mean_x = np.mean(X)
    mean_y = np.mean(Y)
    m = len(X)
    num = 0
    den = 0
    for i in range(m):
        num += (X[i] - mean_x) * (Y[i] - mean_y)
        den += (X[i] - mean_x) ** 2
    b1 = num / den
    b0 = mean_y - (b1* mean_x)
    y=b1*x
    return y
def info(request):
    return render(request,"info.html")
def wheat(request):
    return render(request,"Wheat.html")
