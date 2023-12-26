from django.shortcuts import render, redirect
from .models import books
from .serializers import bookserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

def index(request):
    return render (request, 'index.html')

@api_view(['GET'])
def getall(request):
    if request.method=='GET':
        bookdata=books.objects.all()
        serial=bookserializer(bookdata, many=True)
        return Response (data=serial.data, status=status.HTTP_200_OK)
    else:
        return Response (status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        bookdata=bookserializer(data=request.data)
        if bookdata.is_valid():
            bookdata.save()
            return Response (status=status.HTTP_201_CREATED)
        else:
            return Response (status=status.HTTP_406_NOT_ACCEPTABLE)

def delete(request):
    if request.method == 'GET':
        bookdata = books.objects.all()
        serial = bookserializer(bookdata, many=True)
        return render(request, 'delete.html', {'bookdata': serial.data})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'GET'])
def deleteid(request, id):
    try:
        bookid=books.objects.get(id=id)
    except books.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=bookserializer(bookid)
        return Response (data=serial.data, status=status.HTTP_200_OK)
    
    if request.method=='DELETE':
        books.delete(bookid)
        return redirect ('getall')

def update(request):
    if request.method == 'GET':
        bookdata= books.objects.all()
        serial=bookserializer(bookdata, many=True)
        return render (request, 'update.html', {'bookdata': serial.data})
    else:
        return Response (status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET'])    
def updateid(request, id):
    try:
        bookid=books.objects.get(id=id)
    except books.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial=bookserializer(bookid)
        return Response (data=serial.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        bookdata=bookserializer (data=request.data, instance=bookid)
        if bookdata.is_valid():
            bookdata.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response (status=status.HTTP_400_BAD_REQUEST)