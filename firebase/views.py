from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
import firebase_admin
from firebase_admin import auth, credentials, exceptions

cred = credentials.Certificate('static/credible-bank-235605-firebase-adminsdk-m0fwj-e6b033b006.json')
default_app = firebase_admin.initialize_app(cred)

# Create your views here.
def userList(request):
    if('email' in request.GET):
        result = auth.list_users().iterate_all()
        users = []
        for user in auth.list_users().iterate_all():
            if(user.email != request.GET['email']):
                users.append({"uid":user.uid,"email":user.email,"name":user.display_name,"photo_url":user.photo_url,})
        return JsonResponse(users,safe=False)
    else:
        return JsonResponse("error request",safe=False)
    
    