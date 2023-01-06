from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import SignupRecord
from .forms import SignupForm


# Create your views here.
def signup(request):
    context = {}
    context['form'] = SignupForm()

    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        gender = request.POST['gender']
        dob = request.POST['dob']
        country = request.POST['country']
        password = request.POST['password']
        user_data = SignupRecord(name=name, email=email, gender=gender, dob=dob, country=country, password=password)
        user_data.save()
        print()
        print(user_data)
        messages.success(request, "You are signup sucessfully.")
    return render(request, 'signup.html', context)


def loginn(request):
    if request.method=='POST':
        log_email = request.POST['email']
        log_pass = request.POST['password']
        userlogin=authenticate(username=log_email,password=log_pass)



        if userlogin is not None:
            login(request,userlogin)
            messages.success(request,"you are sucessfully logged in")

            return redirect('/index.html/')
        else:
            messages.error(request,"invalid details, Please try again!!")
            print()
            print('errorr')
    return render(request, 'login.html',userlogin)
