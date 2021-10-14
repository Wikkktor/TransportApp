from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views import View
from register.forms import LoginForm, RegisterForm


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        next_url = request.GET.get('next', '/')
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect(next_url)
            else:
                return HttpResponse("Błędne dane logowania")
        return render(request, 'registration/login.html', {'form': form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect("base")


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_password = form.cleaned_data.get('password')
            user.set_password(user_password)
            user.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect('base')
        return HttpResponse("Coś poszło nie tak")


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/register.html', {'form': form})
