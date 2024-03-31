from django.shortcuts import render

from .forms import DjangoForm, Model_Form

# Create your views here.

def django_form(request):
    if request.method == "POST":
        form = DjangoForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            file = form.cleaned_data['file']
            with open('./app/upload/'+file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
        return render(request,'app/DjangoForm.html',{'form':form})
    else:
        form = DjangoForm()
        return render(request, 'app/DjangoForm.html',{'form':form})

def model_form(request):
    if request.method == "POST":
        form = Model_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return render(request, 'app/ModelForm.html',{'form':form})
    else:
        form = Model_Form()
        return render(request, 'app/ModelForm.html',{'form':form})