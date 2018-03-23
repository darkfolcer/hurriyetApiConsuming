from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.db import models,IntegrityError
from hurriyetApiConsuming.forms import RegisterForm
from django.forms import inlineformset_factory
from django.contrib.auth import (login as auth_login,logout,authenticate)
from hurriyetApiConsuming.emailauth import EmailBackend
from hurriyetApiConsuming.models import Paths
from hurriyetApiConsuming.services import getPaths

def register(request):
    if(request.user.is_authenticated):
        return HttpResponseRedirect('account/preferences')
    _message = 'register new account'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            _email = form.cleaned_data['email']
            _password = form.cleaned_data['password']
            try:
             user = User.objects.create_user(_email,email = _email, password = _password)
             form_user = form.save(commit = False)
             form_user.user = user
             form_user.save()
             return HttpResponseRedirect('/')
            except IntegrityError as e: 
                  _message = 'user already exist.'  
                  context = {'message': _message, 'form': RegisterForm}
                  return render ( request, 'hurriyetApiConsuming/register.html', context )           
        else:
            form = RegisterForm()
            context = {'message': _message}
            return render ( request, 'hurriyetApiConsuming/register.html', context ,)

    else:
       context = {'message': _message, 'form': RegisterForm, 'request' : request}
    return render ( request, 'hurriyetApiConsuming/register.html', context)


def login(request):
    if(request.user.is_authenticated):
        return HttpResponseRedirect('account/preferences')
    oku = request.user.id
    _message = 'sign in'
    if request.method == 'POST':
        _email = request.POST['email']
        _password = request.POST['password']
        customBackend = EmailBackend()
        user = customBackend.authenticate(_email,_password)
        if user is not None:
            if user.is_active:
                auth_login(request,user)
                return HttpResponseRedirect('account/preferences')
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid login, please try again.'
    context = {'message': _message, 'request' : request}
    return render(request, 'hurriyetApiConsuming/login.html', context)


