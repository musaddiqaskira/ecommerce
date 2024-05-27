from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, SignupForm

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        invalid = False
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('shop:product_list')

                else:
                    return HttpResponse('Disabled account')
            else:
                invalid = True
        return render(request, 'account/login.html', {'form': form, 'invalid': invalid})
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponse('User registered')
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('shop:product_list')
