from django.shortcuts import render
import json
from .models import books
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

# Create your views here.

@csrf_exempt
def create_book(request):
    if request.method == 'POST':
        decoded_body = request.body.decode('UTF-8')
        body = json.loads(decoded_body)

        errors = []

        if body['title'] == '':
            errors.append({'title':'Title is required'})
        
        if body['author'] == '':
            errors.append({'author':'Author is required'})
        
        if body['stock'] == '':
            errors.append({'stock':'Stock is required'})
        
        if body['date'] == '':
            errors.append({'date':'Date is required'})
        
        if body['price'] == '':
            errors.append({'price':'Price is required'})
        
        if body['genre'] == '':
            errors.append({'genre':'Genre is required'})
        
        if body['description'] == '':
            errors.append({'description':'Description is required'})

        if len(errors) > 0:
            return JsonResponse({'errors': errors},  status=400)

        book = books.objects.create(
            title=body['title'], 
            author=body['author'],
            stock=body['stock'],
            price=body['price'],
            date=body['date'],
            genre=body['genre'],
            description=body['description']
        )

        return JsonResponse(data={'message': 'book create successful',  'title': book.title, 'author': book.author})
    return HttpResponse('method not allowed', status = 405)



@csrf_exempt
def  get_books(request):
    if request.method == 'GET':
        books_list = list(books.objects.all().values("id", "title", "author", "stock", "price", "date", "genre", "description"))
        return JsonResponse(data={'All books showed successful ': books_list})
    return HttpResponse('method not allowed',  status = 405)

# return  JsonResponse(data={'message': 'All books showed  successful', 'id': books_list.id, 'title': books_list.title, 
#                             'author': books_list.author, 'stock': books_list.stock, 'price': books_list.price, 'date': books_list.date,
#                             'genre': books_list.genre, 'description': books_list.description})


@csrf_exempt
def  get_book(request, id):
    if request.method == 'GET':
        book = books.objects.get(id=id)
        return JsonResponse(data={'book showed successful ': book.title, 'author': book.author, 'stock': book.stock,  
                                'price': book.price, 'date': book.date, 'genre': book.genre, 'description': book.description})
    return HttpResponse('method not allowed',  status = 405)


@csrf_exempt
def  update_book(request, id):
    if request.method == 'PUT':
        if(id):
            body = request.body.decode('UTF-8')
            request_body = json.loads(body)
            
            book = books.objects.get(id = id)
            book.title = request_body.get('title', book.title)
            book.author = request_body.get('author', book.author)
            book.stock = request_body.get('stock', book.stock)
            book.price = request_body.get('price', book.price)
            book.date = request_body.get('date', book.date)
            book.genre = request_body.get('genre', book.genre)
            book.description = request_body.get('description', book.description)

            book.save()

            return JsonResponse(data={
                'message': 'book update successful',
                'title': book.title, 
                'author': book.author,
                'stock': book.stock, 
                'price': book.price,
                'date': book.date,
                'genre': book.genre,
                'description': book.description
            })


@csrf_exempt
def  delete_book(request, id):
    if request.method == 'DELETE':
        if(id):
            book = books.objects.get(id=id)
            book.delete()
            return  JsonResponse(data={'book deleted successful'})
    return  HttpResponse('method not allowed',  status = 405)










