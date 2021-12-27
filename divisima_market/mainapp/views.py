from django.shortcuts import render
from django.views.generic import ListView


class Index(ListView):
    template_name = 'mainapp/index.html'
    queryset = []
