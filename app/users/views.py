from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from carts.models import Cart
from .forms import UserLoginForm,UserRegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required



def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('main:main'))

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            
            session_key=request.session.session_key # ДЛЯ НЕЗАРЕГ ПОЛЬЗОВАТ переб корзину при авторизац
            
            
            if user is not None:
                auth.login(request, user)
                messages.success(request, f'{email}, login is successful')
                
                if session_key:# ДЛЯ НЕЗАРЕГ ПОЛЬЗОВАТ переб корзину при авторизац
                    Cart.objects.filter(session_key=session_key).update(user=user)# ДЛЯ НЕЗАРЕГ ПОЛЬЗОВАТ переб корзину при авторизац
                
                redirect_page=request.POST.get('next',None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                return redirect(reverse('main:main'))
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = UserLoginForm()

    context = {'title': 'Home-authorization', 'form': form}
    return render(request, 'users/login.html', context)



def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('main:main'))
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            
            session_key=request.session.session_key # ДЛЯ НЕЗАРЕГ ПОЛЬЗОВАТ переб корзину при авторизац
            
            user=form.instance
            auth.login(request, user)
            
            if session_key:# ДЛЯ НЕЗАРЕГ ПОЛЬЗОВАТ переб корзину при авторизац
                    Cart.objects.filter(session_key=session_key).update(user=user)# ДЛЯ НЕЗАРЕГ ПОЛЬЗОВАТ переб корзину при авторизац
            
            messages.success(request,f'{user.username} registration is successful')
            return redirect(reverse('main:main'))
    else:
        form =UserRegisterForm()
    context= {'title': 'Home-registration',
              'form': form}
    return render(request, 'users/registration.html', context)



@login_required
def logout(request):
    auth.logout(request)
    messages.success(request,f'{request.user.username} exit from account')
    return redirect(reverse('user:login'))



def user_cart(request):
    return render(request,'users/cart.html')