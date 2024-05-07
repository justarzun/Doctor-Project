from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html/', views.about, name='about'),
    path('index.html/', views.index, name='index'),
    path('services.html/', views.services, name='services'),
    path('blog.html/', views.blog, name='blog'),
    path('contact.html/', views.contact, name='contact'),
    path('contactform/', views.contactform, name='contactform'),
    path('bookingform/', views.bookingform, name='bookingform'),
    
]