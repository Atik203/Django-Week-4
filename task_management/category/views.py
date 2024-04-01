from django.shortcuts import redirect, render

from .forms import CategoryForm

# Create your views here.

def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:    
        return render(request, 'add_category.html', {'form': form})
     