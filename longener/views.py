from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .utils import newURL
from .forms import URLLongenerForm
from .models import MyURL

# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        state = "post"
        form = URLLongenerForm(request.POST)
        if form.is_valid():
            formerURL = form.cleaned_data['formerURL']
            # customURL = form.cleaned_data['customURL']
            new_url = MyURL(former_url=formerURL, new_url=newURL())
            new_url.save()
        else: 
            print(form.errors)
    else:
        state = "get"
        form = URLLongenerForm()
    template = loader.get_template('longener/index.html')
    context = {'form': form, 'state': state}
    return HttpResponse(template.render(context, request=request))

def redirection(request, slug):
    my_redirect = get_object_or_404(MyURL, new_url=slug)
    return redirect(my_redirect.former_url)