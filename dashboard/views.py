from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Aluno

# Create your views here.

class IndexView(generic.ListView):
    template_name = "dashboard/index.html"
    context_object_name = "alunos_list"

    def get_queryset(self):
        return Aluno.objects.order_by('matricula')

class DetailView(generic.DetailView):
    model = Aluno
    template_name = 'dashboard/detail.html'