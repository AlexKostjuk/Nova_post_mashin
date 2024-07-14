from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from user.forms import LoginForm


# Create your views here.

def login_view (request):
   context = {}
   if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():
         user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
         if user is not None:
            login(request, user)
            return redirect('/user/')
      context['error'] = 'invalid username or pasword'
   context['form'] = LoginForm()
   return render(request, 'login.html', context=context)


def logout_view(request):
   logout(request)
   return redirect('/login/')


def register_view(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      email = request.POST['email']
      fname = request.POST['fname']
      lname = request.POST['lname']
      user = User.objects.create_user(username=username, email=email, password=password, first_name=fname, last_name=lname)
      user.save()
      return redirect('/login/')
   else:
      return render(request, 'register.html')


@login_required
def user_page (request):
   return render(request, 'user_page.html', context={'username' : request.user.username, 'email' : request.user.email})
