from django.urls import path, include
from TodoApp import views
from django import views as dj_views

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.addTodo, name="add"),
    path('complete/<todo_id>/', views.completeTodo, name="complete"),
    path('undo/<todo_id>/', views.undoComplete, name="undocomplete"),
    path('deletecompleted/', views.deleteCompleted, name="deletecompleted"),
    path('deleteall/', views.deleteAll, name="deleteall"),
]
