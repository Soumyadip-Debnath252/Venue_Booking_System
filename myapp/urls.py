from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('about', views.about, name="about-page"),
    path('contact', views.contact, name="contact-page"),
    path('reg', views.RegLog, name="reg-page"),
    path('register', views.Register, name="register-page"),
    path('login', views.userLogin, name="Login-page"),
    path('logout', views.usrLogout, name="logout-page"),
    path('catalouge', views.catalouge, name="Catalouge-page"),
    path('book/<int:vid>', views.book, name="book-page"),
    path('bookdetails', views.bookingDetails, name="book-histroy")
]


