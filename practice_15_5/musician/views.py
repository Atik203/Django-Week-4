from django.shortcuts import redirect, render

from .forms import MusicianForm
from .models import Musician

# Create your views here.

def add_musician(request):
    form = MusicianForm()
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_musician')
    else:    
        return render(request, 'add_musician.html', {'form': form})
def edit_musician(request, id):
    musician = Musician.objects.get(pk=id)   
    form = MusicianForm(instance=musician)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return render(request, 'add_musician.html', {'form': form})    

def delete_musician(request, id):
    musician = Musician.objects.get(pk=id)
    musician.delete()
    return redirect('home')    