from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from mysite import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'polls/index.html')

def signup(request):
    
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if User.objects.filter(username = username):
            messages.error(request, "Mr man shey u dey whine me nii use anoda username jhoor")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "Mr man change this email be4 i nack u 2 by 2 for head")
            return redirect("home")
        
        if len(username)>10:
            messages.error(request, "plz no vex oo u dey write all your family name nii abi y u your name go long reach this rubbish change ham jhoor")
        
        if password1 != password2:
            messages.error(request, "Mr man shey u deu whine me nii abi u dey play with your brain check your password jhoor. My Man if u see me again naa beating u go see next niyen")
        
        if not username.isalnum():
            messages.error(request, "Bros u be olodo oo shey u no say username name must be number anf letter")
            return redirect('home')
        myuser = User.objects.create_user(username, email, password1)
        myuser.firs_name = firstname
        myuser.last_name = lastname        
        
        myuser.save()
        
        messages.success(request, "Welldone Sir or Ma")
        
        subject = 'How you be i dey greet u shey u no hear nii'
        message = 'woo' + myuser.first_name + "!! \n" + 'welcome to violence community\n U know the rules\n comfirm your no peace ID to become member og violence slogan no peace.\n\n '
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently = True)
        
        
        
        return redirect('signin')
    return render(request, 'polls/signup.html')

def signin(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        
        user = authenticate(username= username, password = password1)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, "polls/index.html", {'first_name': firstname})
        
        else:
            messages.error(request, "Bad input")
            return redirect('home')
    return render(request, 'polls/signin.html')

def signout(request):
    logout(request)
    messages.success(request, 'Eku Igbadun')
    return redirect("home")
    # return render(request, 'polls/signup.html')