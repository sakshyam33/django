from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def home(request):
    # return HttpResponse("you are at sakshyam's shop")
    return render(request,'website/index.html')
def about(request):
    # return HttpResponse("you are at sakshyam's about")
    return render(request,'website/about.html')
def contact(request):
    # return HttpResponse("you are at sakshyam's contact\n you can contact the number 9865992520")
    return render(request,'website/contact.html')
def SignUppage(request):
    if request.method=="POST":
       uname=request.POST.get('username')
       email=request.POST.get('email')
       pass1=request.POST.get('password1') 
       pass2=request.POST.get('password2')
       if pass1!=pass2:
           return HttpResponse("you have entered the wrong password")
       else:
        my_user=User.objects.create_user(uname,email,pass1,pass2)  
        my_user.save()
    #    return HttpResponse("user has been created successfully")#is for checking only and if check dont use but redirect
        return redirect('login')
    return render(request,'signup.html')
def LoginPage(request):
    if request.method=="POST":
       username=request.POST.get('username')
       pass1=request.POST.get('pass')
       user=authenticate(request,username=username,password=pass1)
       if user is not None:
          login(request,user)
          return redirect('home')
       else:
          return HttpResponse(("Username or password is wrong"))
    return render(request,'login.html')
def Logout(request):
    logout(request)
    return redirect('login')
