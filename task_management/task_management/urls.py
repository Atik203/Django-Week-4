
from django.contrib import admin
from django.urls import include, path

from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('task.urls')),
    path('category/', include('category.urls')),
    path('', home, name='home'),
]
