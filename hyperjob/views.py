from django.views import View
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.http import Http404

nav_links = {'Login': '/login',
             'Sign Up': '/signup',
             'Vacancies': '/vacancies',
             'Resumes': '/resumes',
             'Home': '/home',
             'Logout': '/logout'}


class MainPage(View):
    def get(self, requests, *args, **kwargs):
        return render(requests, 'hyperjob/main.html', context={'nav_links': nav_links})


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'hyperjob/signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'hyperjob/login.html'


class HomePageView(View):
    def get(self, requests, *args, **kwargs):
        template_name = 'hyperjob/home.html'
        context = {'username': 'Not logged in',
                   'last_login': 'N/A',
                   'is_staff': False}
        if requests.user.is_authenticated:
            # if requests.user.is_staff:
            #     return redirect('vacancy/new')
            # else:
            #     return redirect('resume/new')
            context = {'username': requests.user.username,
                       'last_login': requests.user.last_login,
                       'is_staff': requests.user.is_staff
            }
        return render(requests, template_name=template_name, context=context)
