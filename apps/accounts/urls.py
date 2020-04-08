from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    #user
    path('', views.list_users, name='list_users'),
    path('login/', views.user_login, name='user_login'),
    path('cadastro/', views.add_user_register, name='add_user_register'),
    path('logout/', views.user_logout, name='user_logout'),
    path('alterar-senha/', views.user_change_password, name='user_change_password'),
    path('novo-perfil/', views.add_user_profile, name='add_user_profile'),
    path('perfil/', views.list_user_profile, name='list_user_profile'),
    path('adicionar/', views.add_user, name='add_user'),
    path('alterar-perfil/<username>/', views.change_user_profile, name='change_user_profile'),
    path('alterar-cadastro/<username>/', views.change_user_information, name='change_user_information'),
    #path('editar/<int:id_user>/', views.edit_user, name='edit_user'),
    #path('apagar/<int:id_user>/', views.delete_user, name='delete_user'),
]
