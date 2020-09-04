from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .utils import newURL

# Create your views here.
def index(request):
    message = newURL()
    template = loader.get_template('longener/index.html')
    context = {'message': message}
    return HttpResponse(template.render(context,request=request))

