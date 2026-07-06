from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('player/',views.player_list, name='player_list'),
    path('create/', views.player_create, name='player_create'),
    path('update/<int:pk>/', views.player_update, name='player_update'),
    path('delete/<int:pk>/', views.player_delete, name='player_delete'),
    
]