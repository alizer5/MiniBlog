from django.shortcuts import render ,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from  .forms import SignupForm,LoginForm,PostForm,CommentsForm
import requests
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Postblog
from django.contrib.auth.models import Group
def home(req):
    posts=Postblog.objects.all()
    return render(req,'home.html',{'posts':posts})

def about(req):
    return render(req,'about.html')


def contact(req):
    if req.method=="POST":
        form=CommentsForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,'Message sent SuccessFully')
            form=CommentsForm()
            # return HttpResponseRedirect('/thankyou')
    else:
        form=CommentsForm()
    return render(req,'contact.html',{'form':form})

def dashboard(req):
    if req.user.is_authenticated:
        posts=Postblog.objects.all()
        return render(req,'dashboard.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login Successfully')
                    return HttpResponseRedirect('/dashboard/')  # Use 'dashboard' view name
                else:
                    messages.error(request, 'Invalid login credentials')  # Handle invalid login
        else:
            form = LoginForm()
        
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')  
    
def user_signup(req):
    if req.method=='POST':
        form=SignupForm(req.POST)
        if form.is_valid():
         messages.success(req,'User Added SuccessFully')
         user=form.save()
         group=Group.objects.get(name="Author")
         user.groups.add(group)
         
    else:
     form=SignupForm()
    return render(req,'signup.html',{'form':form})

def user_logout(req):
    logout(req)
    return HttpResponseRedirect('/')


def add_post(req):
    if req.user.is_authenticated:
         if req.method == "POST":
             form=PostForm(req.POST)
             if form.is_valid():
                form.save()
                form=PostForm()
                messages.success(req, 'Data Added SuccessFully')
         else:
             form=PostForm()         

         return render(req,'add.html',{'form':form})
    else:
     return  HttpResponseRedirect('/login/')
    

def update_post(req, id):
    if req.user.is_authenticated:
        pi = Postblog.objects.get(id=id)
        
        if req.method == "POST":
            form = PostForm(req.POST, instance=pi)
            if form.is_valid():
                form.save()
                messages.success(req, 'Blog Updated Successfully')
                return HttpResponseRedirect('/dashboard/')  
        else:
            form = PostForm(instance=pi)  
        return render(req, 'update.html', {'form': form})
    
    else:
        return HttpResponseRedirect('/login/')

    

def delete_post(req,id):
     if req.user.is_authenticated:
            if req.method=="POST":
                pi=Postblog.objects.get(id=id)
                pi.delete()
                
            return HttpResponseRedirect('/dashboard/') 

     else:
         return HttpResponseRedirect('/login/')