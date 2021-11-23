from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Destination


# Create your views here.
def home(request):
    return render(request, 'home.html')


# login

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid User')
            return redirect('/')
    else:
        return render(request, 'login.html')


# logout

def logout(request):
    auth.logout(request)
    return redirect('/')
    # User Authentication

    # def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        Cpassword = request.POST['Cpassword']

        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                        last_name=last_name)
        user.save();
        print('User Created')
        return redirect('/')

    else:
        return render(request, 'register.html')


def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        birth_date = request.POST['birth_date']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        blood_group = request.POST['blood_group']
        contact_number = request.POST['contact_number']
        email = request.POST['email']
        password = request.POST['password']
        Cpassword = request.POST['Cpassword']
        message = request.POST['message']
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                        last_name=last_name)

        destination = Destination(first_name=first_name, last_name=last_name, username=username,
                                  birth_date=birth_date, country=country, state=state, city=city,
                                  blood_group=blood_group, contact_number=contact_number, email=email,
                                  message=message)
        user.save()
        destination.save()
        print('Registration Successful')
        return redirect('login')
    else:
        return render(request, 'register.html')
