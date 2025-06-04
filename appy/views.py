from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from appy.models import Students
from appy.serializer import StudentSerializer


# Create your views here.
@api_view(['POST'])
def save(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def fetch(request):
    # Students.objects.create(name ="Tung Tung Tung", email ="Sahur@example.com", password = "123456", gender = "soccer", education="University ")
    students = Students.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)