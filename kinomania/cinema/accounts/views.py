from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginView(View):
    def get(self,request):
        form = AuthenticationForm(request)
        context = {
            'form': form
        }
        return render(request, 'accounts/login.html', context)

    def post(self,request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')

class RegiseredViews(View):
    def get(self,request):
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/register.html', context)

    def post(self,request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user_obj = form.save()
            return redirect('/login/')

class LogoutViews(View):
    def get(self,request):
        return render(request, 'accounts/logout.html')
    def post(self,request):
        logout(request)
        return redirect('/login/')





