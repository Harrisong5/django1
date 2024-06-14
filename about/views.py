from django.shortcuts import render
from django.http import HttpResponse

def about_me(request):
    return HttpResponse("This would be the about page")

