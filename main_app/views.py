from django.shortcuts import render, redirect
from .models import Widget
from django.views.generic.edit import CreateView

# Create your views here.


def index(request):
    widgets = Widget.objects.all()
    return render(request, 'index.html', {'widgets': widgets})
