from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def review_home(request):
    return HttpResponse("Reviews Working!")
