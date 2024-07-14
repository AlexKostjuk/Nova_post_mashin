from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def login_view (request):
   context = {}
   if request.method == 'POST':
      username = request.POST['username']
      passsword = request.POST['password']
      user = authenticate(username=username, passsword=passsword)
      if user is not None:
         login(request, user)
         return redirect('/user/')
      else:
         context['error'] = 'invalid username or pasword'
   return render(request, 'login.html', context=context)


def logout_view(request):
   logout(request)
   return redirect('/login/')


def register_view(request):
   if request.method == 'POST':
      username = request.POST['username']
      passsword = request.POST['password']
      email = request.POST['email']
      fname = request.POST['fname']
      lname = request.POST['lname']
      user = User.objects.create_user(username=username, email=email, password=passsword, first_name=fname, last_name=lname)
      user.save()
      return redirect('/login/')
   else:
      return render(request, 'register.html')



def user_page (request):
   return HttpResponse("helo start")
