from django.shortcuts import render, redirect
from django.views import View
from .models import Vacancy
from django.http import HttpResponseForbidden


# Create your views here.
class VacancyPage(View):
    def get(self, requests):
        template_name = 'vacancy/vacancy.html'
        context = {'vacancy': Vacancy.objects.filter()}
        return render(requests, template_name=template_name, context=context)


class CreateVacancyPage(View):
    def get(self, requests):
        template_name = 'vacancy/create_vacancy.html'
        context = {}
        return render(requests, template_name=template_name, context=context)

    def post(self, requests):
        if requests.user.is_staff:
            author = requests.user
            vacancy_desc = requests.POST.get('description')
            vacancy_add = Vacancy.objects.create(author=author, description=vacancy_desc)
            return redirect('/home')
        else:
            return HttpResponseForbidden()
