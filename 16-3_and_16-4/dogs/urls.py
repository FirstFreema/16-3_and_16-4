from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_pets, name='read_pets'),
    path('create/', views.create_pet, name='create_pet'),
    path('update/<int:pk>/', views.update_pet, name='update_pet'),
    path('delete/<int:pk>/', views.delete_pet, name='delete_pet'),
    path('json/', views.list_view, name='list_view'),
    path('breeds/', views.breed_list, name='breed_list'),
    path('list/', views.dog_list, name='dog_list'),  # Переименуйте для избегания путаницы
]
