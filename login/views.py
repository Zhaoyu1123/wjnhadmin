# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index(request):
    return render(request, 'search.html', {})


@login_required
def statistic(request):
    return render(request, 'statistic.html', {})


class LoginView(View):

    error = ""

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                self.error = '账户被冻结'
        else:
            self.error = '用户名或密码错误'
        return render(request, 'login.html', {"error": self.error})


@login_required
def logout(request):
    auth_logout(request)
    return render(request, 'login.html')
