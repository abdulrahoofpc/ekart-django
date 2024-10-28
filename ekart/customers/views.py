from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Customer

def sign_out(request):
    logout(request)
    return redirect('home')
# Create your views here.
def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            #user creating
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            #create customer
            customer= Customer.objects.create(
                user=user,
                phone=phone,
                address=address
                
            )
            success_message="user registred successfully"
            messages.success(request,success_message)
        except Exception as e:
            error_message="Duplicat username or invalid inputs"
            messages.error(request,error_message)

    if request.POST and 'login' in request.POST:
        context['register']=False
        username=username.request.POST('username')
        password=password.request.POST('password')
        user=authenticate(username=username,
                          password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid user')

    return render(request,'account.html')
    
