from django.shortcuts import render,HttpResponse,redirect
from .models import ChaiVarity
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def all(request):
    chais = ChaiVarity.objects.all()
    return render(request,'sakshyam/all_item.html',{'chais': chais})
