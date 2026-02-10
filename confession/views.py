from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    return render(request, 'confession/home.html')

def yes_page(request):
    return render(request, 'confession/yes.html')

def no_page(request):
    return render(request, 'confession/no.html')
