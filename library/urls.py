from .views import create_book, get_books, get_book, update_book, delete_book
from django.urls import  path
# update_book,  delete_book, get_book,
#from .views import delete_book

urlpatterns = [
    path('create_book/', create_book, name='create_book'),
    path('get_books/',  get_books, name='get_books'),
    path('<int:id>/',  get_book, name='get_book'),
    path('update_book/<int:id>/', update_book, name='update_book'),
    path('delete_book/<int:id>/', delete_book, name='delete_book'),
]