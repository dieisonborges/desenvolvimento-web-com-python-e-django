from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    #user
    path('', views.list_users, name='list_users'),
    path('login/', views.user_login, name='user_login'),
    path('adicionar/', views.add_user, name='add_user'),
    #path('editar/<int:id_user>/', views.edit_user, name='edit_user'),
    #path('apagar/<int:id_user>/', views.delete_user, name='delete_user'),
]
