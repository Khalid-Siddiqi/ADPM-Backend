from django.http import HttpResponse
from django.shortcuts import render 
def home(request):
    return render(request, 'website/index.html')
    #return HttpResponse("Hello World You are at ADPM home page")
def about(request):
    return HttpResponse("Hello World You are at ADPM About Us page")
def contact(request,respond):
    return HttpResponse("Hello World You are at ADPM Contact Us page")
