from django.contrib import admin
from django.urls import path

from .views import details, book_create, book_list, home, update, delete

urlpatterns = [
    path('', home, name='home'),
    path('details/<int:pk>', details, name='details'),
    path('create/', book_create, name='create_form'),
    path('update/<int:pk>', update, name='update'),
    path('delete/<int:pk>', delete, name='delete'),

]
