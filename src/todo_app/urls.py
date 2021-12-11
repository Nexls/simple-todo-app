from django.urls import path

from .views import todo_create, todo_delete, todo_detail, todo_list, todo_update

app_name = 'todos'

urlpatterns = [
    path('', todo_list),
    path('create/', todo_create),
    path('<id>/', todo_detail),
    path('<id>/update/', todo_update),
    path('<id>/delete/', todo_delete),
]
