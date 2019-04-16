"""croppred URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from module import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^welcome', views.welcome, name='welcome'),
    url(r'^Signup', views.Signup, name='Signup'),
    url(r'^Login', views.Login, name='Login'),
url(r'^cp', views.cp, name='cp'),
url(r'^pfy', views.pfy, name='pfy'),
url(r'^district', views.district, name='district'),
url(r'^logout', views.logout, name='logout'),
url(r'^videos', views.videos, name='videos'),
url(r'^vplay', views.vplay, name='vplay'),
    url(r'^prediction', views.prediction, name='prediction'),
url(r'^choose', views.choose, name='choose'),
url(r'^roh', views.roh, name='roh'),
url(r'^info', views.info, name='info'),
    url(r'^wheat', views.wheat, name='wheat'),
    url(r'^bajra', views.bajra, name='bajra'),
    url(r'^Shah', views.Shah, name='Shah'),
    url(r'^soh', views.soh, name='soh'),
]
