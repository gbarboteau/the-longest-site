from django import forms

class URLLongenerForm(forms.Form):
    formerURL = forms.CharField(max_length=255)
    customURL = forms.CharField(max_length=1000)