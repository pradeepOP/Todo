from django.urls import path
from . import views

urlpatterns = [
    path('',views.todos, name="todos"),
    path('add_todo/', views.add_todo, name="add-todo"),
    path('update_todo/<int:pk>/', views.update_todo, name="update-todo"),
    path('delete_todo/<int:pk>/', views.delete_todo, name="delete-todo"),
]
