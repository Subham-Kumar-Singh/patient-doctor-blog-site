from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *

# Create your views here.
from .models import *


@login_required(login_url='login')
def home(request):
    return render(request, 'home/home.html')


@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
            messages.success(
                request, "Your message has been successfully sent")
    return render(request, 'home/contact.html')


@login_required(login_url='login')
def about(request):
    return render(request, 'home/about.html')


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password is incorrect")

    context = {}
    return render(request, 'home/login.html', context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        form = CreateUserForm()

        # this post method is taking the input that are given in form and putting it through
        # UserCreationForm method is it is valid then it is saving it .
        # this is the advantage of the django form method
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                user = form.cleaned_data.get('username')

                # this is used to flash a message of success that is imported
                # from django.contrib
                messages.success(request, "account was created for " + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'home/register_patients.html', context)


def logoutPage(request):
    # if request.method=='POST':
    logout(request)
    context = {}
    return render(request, 'home/login.html', context)
