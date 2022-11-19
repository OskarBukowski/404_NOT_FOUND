from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_view, name='adverts'),
    path('<int:pk>/', views.single_advert, name='single_advert'),
]
