from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ExerciseSerializer, UserSerializer
from .models import Exercise, User

# Create your views here.

@api_view(['GET', 'POST'])
def exercise_list(request):
    if request.method == 'GET':
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ExerciseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'PUT'])
def delete_or_edit_user(request, username):
    try:
        user = User.objects.get(username = username)
    except User.DoesNotExsist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)