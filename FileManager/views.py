from django.shortcuts import render

# Create your views here.


def gallery_view(request):
    return render(request, 'FileManager/gallery.html', context={})
