from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World You are at ADPM home page")
def about(request):
    return HttpResponse("Hello World You are at ADPM About Us page")
def contact(request,respond):
    return HttpResponse("Hello World You are at ADPM Contact Us page")
