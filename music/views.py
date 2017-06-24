from django.http import Http404
from django.shortcuts import render
from .models import Album

def index(request):
    # connects to the database
    all_albums = Album.objects.all()

    # http response id built in
    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    # check if data present in database
    try:
        # try to get one album
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album': album})