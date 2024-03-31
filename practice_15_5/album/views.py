from django.shortcuts import redirect, render

from .forms import AlbumForm
from .models import Album


# Create your views here.
def add_album(request):
    form = AlbumForm()
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_album')
    else:    
        return render(request, 'add_album.html', {'form': form})
    
def edit_album(request, id):
    album = Album.objects.get(pk=id)   
    form = AlbumForm(instance=album)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return render(request, 'add_album.html', {'form': form})    
    
def delete_album(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('home')    