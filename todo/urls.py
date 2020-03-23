from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.TodoListView.as_view(), name='home'),
    path('<int:id>/delete/', views.TodoDeleteView.as_view(), name='delete')
]