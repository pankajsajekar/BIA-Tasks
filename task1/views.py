from django.shortcuts import render
from django.http import HttpResponse

# Using fuction Base View
def index(request):
    extra = ""
    txt = "Hello Django!" + extra
    return HttpResponse(txt)