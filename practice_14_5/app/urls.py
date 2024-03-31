from django.urls import path

from .views import django_form, model_form

urlpatterns = [
    path('django-fom/', django_form, name='django_form'),
    path('model-form/', model_form, name='model_form')
]
