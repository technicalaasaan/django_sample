from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Subjects
from django.shortcuts import HttpResponse


# Create your views here.
def welcome(request):
    return HttpResponse("Success")

class SubjectView(CreateView):
    model = Subjects
    fields = ["sub_name", "dept", "year"]
    success_url = "/"

class SubjectUpdateView(UpdateView):
    model = Subjects
    fields = ["sub_name", "dept", "year"]
    success_url = "/"

class SubjectDeleteView(DeleteView):
    model = Subjects
    success_url = "/"
    template_name = "Student/Subjects_delete.html"


class SubjectListView(ListView):
    model = Subjects
    fields = ["sub_name", "dept", "year"]
    template_name = "Student/Subjects_list.html"




