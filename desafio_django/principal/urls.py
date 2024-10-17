from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('image-url', views.image_url, name='image_url'),
]