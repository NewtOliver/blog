from django.shortcuts import render
from picture_app.models import Picture


def index(request):
    pictures = Picture.objects
    return render(request, 'index.html', {'pictures': pictures})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')






