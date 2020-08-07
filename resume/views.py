from django.shortcuts import render, redirect
from django.views import View
from resume.models import Resume
from django.http import HttpResponseForbidden


# Create your views here.
class ResumePage(View):
    def get(self, requests):
        return render(requests, template_name='resume/resume.html', context={'resumes': Resume.objects.filter()})


class CreateResumePage(View):
    def get(self, requests):
        template_name = 'resume/create_resume.html'
        context = {}
        return render(requests, template_name=template_name, context=context)

    def post(self, requests):
        if requests.user.is_authenticated:
            author = requests.user
            resume_text = requests.POST.get('description')
            resume_add = Resume.objects.create(author=author, description=resume_text)
            return redirect('/home')
        else:
            return HttpResponseForbidden()


class DeleteResumeItem(View):
    def post(self, requests):
        if requests.user.is_authenticated:
            try:
                delete_item = Resume.objects.get(description=requests.POST.get('del_desc'))
                delete_item.delete()
            except Resume.DoesNotExist:
                pass
            return redirect('/home')