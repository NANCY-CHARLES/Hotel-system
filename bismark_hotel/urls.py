from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('rooms', views.rooms, name='rooms'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('bookroom/<int:id>/', views.bookroom, name='bookroom'),
    path('roomdetails/<int:id>/', views.roomdetails, name='roomdetails'),
    path('logout', views.logout, name='logout'),
    path('saveroom/<int:id>', views.saveroom, name='saveroom'),
    

]