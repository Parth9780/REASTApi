from django.shortcuts import render,redirect
from .models import BookInfo
from .forms import BookInfoForm
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = BookInfoForm(request.POST)
        if form.is_valid():
            form.save() # redirect to a list view of book info
    else:
        form = BookInfoForm() 
    return render(request,'index.html')

@api_view(['GET'])
def getall(request):
    if request.method=='GET':
        Bdata=BookInfo.objects.all()
        serial = BookSerializer(Bdata,many=True)
        return Response(serial.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getid(request,id):
    try:
        bid = BookInfo.objects.get(id=id)
    except BookInfo.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serial = BookSerializer(bid)
    return Response(serial.data,status=status.HTTP_200_OK)

@api_view(['DELETE','GET'])
def deleteid(request,id):
    try:
        bid = BookInfo.objects.get(id=id)
    except BookInfo.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method=='GET':
        serial = BookSerializer(bid)
        return Response(serial.data,status=status.HTTP_200_OK)
    if request.method=='DELETE':
        BookInfo.delete(bid)
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        serial=BookSerializer(data=request.data)
        if serial.is_valid():
            serial.save() 
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET'])
def updateid(request,id):
    try:
        bid = BookInfo.objects.get(id=id)
    except BookInfo.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method=='GET':
        serial = BookSerializer(bid)
        return Response(serial.data,status=status.HTTP_200_OK)
    if request.method=='PUT':
        serial=BookSerializer(data=request.data,instance=bid)
        if serial.is_valid():
            serial.save() 
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)