from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [

    path('', views.home, name='home'),
    path('delete-todo/<id>/', views.delete, name='delete-todo'),
    path('done-todo/<id>/', views.done, name='todo-done'),
    path('undo-todo/<id>/', views.undo, name='todo-undo'),
]
