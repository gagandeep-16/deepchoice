from django.shortcuts import render,redirect,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login

# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    context = {
        "variable1":"hey Devi", #we are running the variable vale here which is wrtten in html
        "variable2":"hey gagan",
    }
    return render(request,'index.html',context)
   # return HttpResponse("this is homepage")
def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)


        # check if user has entered correct credential
        user = authenticate(username='username', password='password')
        if user is not None:
            login(request,user)
        # A backend authenticated the credentials
            return redirect('home')
        else:
             # No backend authenticated the credentials
            return render(request,'login.html')  

    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")  


def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,'contact.html')
    #return HttpResponse("this is contact page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is services page")
#urls dipatching understood...

