from django.urls import path
from users import views
from .views import create_user, users_list, user_detail, update_user, delete_user



urlpatterns = [
    path('create_user/', create_user, name='createUser'),
    path('users_list/', users_list, name='listUsers'),
    path('<int:id>/', user_detail,  name='detailUser'),
    path('update_user/<int:id>/', update_user,  name='updateUser'),
    path('delete_user/<int:id>/', delete_user,  name='deleteUser'),
]