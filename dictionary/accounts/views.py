from django.shortcuts import render, redirect

from django.contrib import messages
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/register.html', context)

    def post(self, request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('/login')
        else:
            return render(request, 'accounts/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm(request)
        context = {
            'form': form
        }
        return render(request, 'accounts/login.html', context)

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        context = {
            'form': form
        }
        return render(request, 'accounts/login.html', context)


class LogoutView(View):
    def get(self, request):
        return render(request, 'accounts/logout.html')

    def post(self, request):
        logout(request)
        return redirect('/login')
