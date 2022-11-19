from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_view, name='adverts'),
    path('<int:pk>/', views.single_advert, name='single_advert'),
    path('create/', views.create_advert, name='advert_create'),
]
