from django.views import View
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.http import Http404
from resume.models import Resume
from vacancy.models import Vacancy

nav_links = {'Login': '/login',
             'Sign Up': '/signup',
             'Vacancies': '/vacancies',
             'Resumes': '/resumes',
             'Home': '/home',
             'Logout': '/logout'}


class MainPage(View):
    def get(self, requests, *args, **kwargs):
        return render(requests, 'hyperjob/start.html', context={'nav_links': nav_links})


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
        context = {'username': None,
                   'last_login': 'N/A',
                   'is_staff': False,
                   'tab_data': None}
        if requests.user.is_authenticated:
            if requests.user.is_staff:
                tab_data = Vacancy.objects.filter(author=requests.user)
            else:
                tab_data = Resume.objects.filter(author=requests.user)
            context = {'username': requests.user.username,
                       'last_login': requests.user.last_login,
                       'is_staff': requests.user.is_staff,
                       'tab_data': tab_data
            }
        return render(requests, template_name=template_name, context=context)
