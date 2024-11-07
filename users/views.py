from django.shortcuts import render
import json
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse


# Create your views here.

@csrf_exempt
def users_list(request):
    if request.method == 'GET':
        users = list(CustomUser.objects.all().values('id', 'username', 'password', 'email', 'buy', 'comment', 'phone_number'))
        return JsonResponse(data={'All Users:': users})
    # {'message': 'All users showed succesfull', 'id': users.id, 'username': users.username, 'password': users.password, 'email': users.email, 'birthday': users.birthday, 'biography': users.biography
    return HttpResponse(content='Method not allowed', status=405)


@csrf_exempt
def user_detail(request, id):
    if request.method == 'GET':
        if(id):
            user = CustomUser.objects.get(id=id)
            return JsonResponse(data={"message": "Ok", "id":  user.id, "UserName":  user.username, 
                                "Password":  user.password, "Email":  user.email, "Buy": user.buy, "Comment": user.comment, "Phone Number":  user.phone_number})


    return JsonResponse(data={"message": "User was sucessfull showed", "User": user })


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        docoded_body = request.body.decode('UTF-8')
        body = json.loads(docoded_body)

        errors = []
        
        if body['username'] == '':
            errors.append({'username': 'Username cannot be empty'})
        
        if body['phone_number'] == '':
            errors.append({'birthday': 'Date format invalid'})
        
        if body['email'] == '':
            errors.append({'email': 'Invalid email format'})

        if len(errors) > 0:
            return JsonResponse({'errors': errors}, status = 400)
        
        user = CustomUser.objects.create(
            username = body['username'],
            password = body['password'],
            email = body['email'],
            buy = body['buy'],
            comment = body['comment'],
            phone_number = body['phone_number']
        )

        return JsonResponse(data={'message': 'CustomUser create succesful', 'id': user.id, 'username': user.username})
    
    return HttpResponse('method not allowed', status = 405)

@csrf_exempt
def update_user(request, id):
    if request.method == 'PUT':

        if(id):

            body = request.body.decode('utf-8')
            request_body = json.loads(body)

            user = CustomUser.objects.get(id = id)
            user.username = request_body.get('username', user.username)
            user.password = request_body.get('password', user.password)
            user.email = request_body.get('email', user.email)
            user.buy = request_body.get('buy', user.buy)
            user.comment = request_body.get('comment', user.comment)
            user.phone_number = request_body.get('phone_number', user.phone_number)

            user.save()

            return JsonResponse(data={
                'message': 'User Update Succesfull',
                'username': user.username,
                'password': user.password,
                'email': user.email,
                'buy': user.buy,
                'comment': user.comment,
                'phone_number': user.phone_number,
            })

@csrf_exempt
def delete_user(request, id):
    if request.method == 'DELETE':
        if(id):

            CustomUser.objects.get(id = id).delete()
        return JsonResponse(data={'message': 'User succesfully delete'})