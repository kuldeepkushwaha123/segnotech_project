from django.shortcuts import render,HttpResponse
from .models import Contact
from django.contrib import messages
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login,logout
# Create your views here.


def home(request):
    return render(request,'Home/home.html')

def about(request):
    return render(request, 'Home/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)< 10 or len(content)< 4:
            messages.error(request, "Please fill the form correctly !!")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,'Your message has been  send !!')
    return render(request, 'Home/contact.html')



def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        ''' check for error inputs '''
        if len(username) > 10:
            messages.error(request, "username must be under 10 character please signup again ")
            return redirect('home')
        if len(username) < 5:
            messages.error(request, "username must be 5 character above ")
            return redirect('home')
        if not username.isalnum():
            messages.error(request,'username should only contain letters and numbers')
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, "password do not match")
            return redirect('home')

        ''' Create the user'''

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('home')



    else:
        return HttpResponse('404 - Not Found')




def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername ,password = loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully Logged In')
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials, Please try again ")
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')



def handleLogout(request):
    print('logoouuutut')
    logout(request)
    messages.success(request,"Successfully logged Out!")
    return redirect('home')