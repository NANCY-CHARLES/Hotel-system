from django.urls import path
from . import views
from .views import *

urlpatterns= [
path('', views.users, name='users'),
path('bookings', views.bookings, name='bookings'),
path('room', views.room, name='room'),
path('messages', views.messages, name='messages'),
path('edit/<int:id>', views.edit, name='edit'),
path('update/<int:id>', views.update, name='update'),
path('delete/<int:id>', views.delete, name='delete')

]