from django.shortcuts import render,get_object_or_404
from picture_app.models import Picture
# Create your views here.


def pictures(request):
    pictures = Picture.objects
    return render(request, 'pictures.html', {'pictures': pictures})


def picture_detail(request, picture_id):
    print(picture_id)
    picture = get_object_or_404(Picture, pk=picture_id)
    return render(request, 'pictures-detail.html', {'picture': picture})
