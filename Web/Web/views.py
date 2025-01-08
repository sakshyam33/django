from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from sakshyam.forms import ContactForm
from django.contrib import messages

def home(request):
    # return HttpResponse("you are at sakshyam's shop")
    return render(request,'website/index.html')
def about(request):
    # return HttpResponse("you are at sakshyam's about")
    return render(request,'website/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Use the form class
        if form.is_valid():
            form.save()  # Save the form data to the database  
            return redirect('contact')
        else:
             return render(request,'website/error.html',{'errormessage':'your form data is invalid'})     
    else:
        form = ContactForm()  # Empty form for GET request
        return render(request, 'website/contact.html', {'form': form})  # Pass form to template

    # return render(request, 'website/contact.html', {'form': form})  # Pass form to template


def SignUppage(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1') 
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("You have entered the wrong password")
        
        if User.objects.filter(username=uname).exists():
            return HttpResponse("Username already exists")
        
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already exists")

        my_user = User.objects.create_user(username=uname, email=email, password=pass1)
        my_user.save()
        
        # Add a success message
        messages.success(request, "Your account has been successfully created. You can now log in.")

        return redirect('login')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user exists
        user = User.objects.filter(username=username).first()

        if user is None:
            messages.error(request, "Username does not exist.")
            return redirect('login')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Incorrect password.")
            return redirect('login')

    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('login')
