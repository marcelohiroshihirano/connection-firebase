from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.utils import timezone
import json 
from pyrebase import pyrebase
# Create your views here.

config = {
    'apiKey': "AIzaSyCEg5O8Sl5ptYLvGc_IaU-vOukrHlTWHwA",
    'authDomain': "araddin-sample.firebaseapp.com",
    'databaseURL': "https://araddin-sample.firebaseio.com",
    'projectId': "araddin-sample",
    'storageBucket': "araddin-sample.appspot.com",
    'messagingSenderId': "180601055010",
    'appId': "1:180601055010:web:ac7f68e7f478d76f80677b"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
@api_view(['GET','POST'])    
def list_courses(request):
    try:
        #email=request.POST.get('marcelohiroshi@mgmail.com')
        #passw = request.POST.get('marcelohiroshi@mgmail.com')
        user = auth.sign_in_with_email_and_password('marcelohiroshi@gmail.com','12345678')
        db = firebase.database()
    except:
        return Response('エラー　admin ご連絡してください！')
    if request.method == "GET":
       all_users = db.child("marcelohiroshi@gmail").get() 
       return Response(all_users.val())
    elif request.method == 'POST':
        #create
        #name = request.POST.get('name')
        #age = request.POST.get('age')
        #sex = request.POST.get('sex')
        teste = json.loads(request.POST.get('data',''))
        #data = {"age": age,"name":name,"sex":sex}
        #db.child("marcelohiroshi@gmail").push(data)
        print(teste)
        return Response(teste['Respostas'])  # Successful post
    else:  
        return Response("エラーadminご連絡ください")  #Invalid data

@api_view(['DELETE','PUT'])
def course_details(request, id):
    try:
        user = auth.sign_in_with_email_and_password('marcelohiroshi@gmail.com','12345678')
        db = firebase.database()
    except:
        return Response('エラー　admin ご連絡してください！')
    if request.method == 'PUT': 
        #update
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        data = {"age": age,"name":name,"sex":sex}
        db.child("marcelohiroshi@gmail").child(id).update(data)   
        return Response('変更できました')        
        
    elif request.method == 'DELETE':
        db.child("marcelohiroshi@gmail").child(id).remove()
        return Response('削除できました')
    else:
        return Response('登録されているできませんでした')  # Bad request
