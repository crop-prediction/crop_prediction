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
    if nm == "Wheat":
        y=WheatPred(x)
    elif nm=="Bajra":
        y=BajraPred(x)
    elif nm=="Chillies":
        y=ChiliPred(x)
    elif nm=="Groundnut":
        y=GroundnutPred(x)
    elif nm=="Sugarcane":
        y=SugarcanePred(x)
    elif nm=="Peas":
        y=PeasPred(x)
    elif nm=="Rice":
        y=RicePred(x)
    else:
        y=JowarPred(x)
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
def bajra(request):
    return render(request,"Bajra.html")
def ChiliPred(x):
    print("h3")
    data=pd.read_csv('F:\crop\croppred\module\data3.csv')
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
def SugarcanePred(x):
    print("h2")
    data=pd.read_csv('F:\crop\croppred\module\data8.csv')
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
def PeasPred(x):
    data=pd.read_csv('F:\crop\croppred\module\data7.csv')
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
def GroundnutPred(x):
    print("h2")
    data=pd.read_csv('F:\crop\croppred\module\data6.csv')
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
def JowarPred(x):
    print("h2")
    data=pd.read_csv('F:\crop\croppred\module\data5.csv')
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
def RicePred(x):
    data=pd.read_csv('F:\crop\croppred\module\data4.csv')
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
def bajra(request):
    return render(request,"Bajra.html")
def DeoriaWheat(x,yr):
    data=pd.read_csv('F:\crop\croppred\module\DeoriaWheat.csv')
    X=data['Crop_Year'].values
    Y=data['P/A'].values
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
    y=b1*yr+b0
    y=y*x
    return y
def DeoriaBajra(x,yr):
    data=pd.read_csv('F:\crop\croppred\module\DeoriaBajra.csv')
    X=data['Crop_Year'].values
    Y=data['P/A'].values
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
    y=b1*yr+b0
    y=y*x
    return y
def HathrasWheat(x,yr):
    data=pd.read_csv('F:\crop\croppred\module\HathrasWheat.csv')
    X=data['Crop_Year'].values
    Y=data['P/A'].values
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
    y=b1*yr+b0
    y=y*x
    return y
def HathrasBajra(x,yr):
    data=pd.read_csv('F:\crop\croppred\module\HathrasBajra.csv')
    X=data['Crop_Year'].values
    Y=data['P/A'].values
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
    y=b1*yr+b0
    y=y*x
    return y
def Shah(request):
    return render(request,"Shah.html")
def soh(request):
    x=int(request.GET.get("area"))
    nm=str(request.GET.get("crop"))
    dist=str(request.GET.get("dist"))
    yr=int(request.GET.get("yr"))
    if dist=='Deoria' and nm=='Wheat':
        y=DeoriaWheat(x,yr-1996)
    if dist=='Deoria' and nm=='Bajra':
        y=DeoriaBajra(x,(yr-1996)/10)
    if dist=='Hathras' and nm=='Wheat':
        y=HathrasWheat(x,(yr-1996)/10)
    if dist=='Hathras' and nm=='Bajra':
        y=HathrasBajra(x,(yr-1996)/10)
    return render(request,"production2.html",{"prod":y,"crop":nm,"area":x,"year":yr,"dist":dist})


