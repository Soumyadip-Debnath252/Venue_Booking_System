from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('about', views.about, name="about-page"),
    path('contact', views.contact, name="contact-page"),
    path('catalouge', views.catalouge, name="catalouge-page"),
    path('Registration', views.Registration, name="Registration-page")
]
