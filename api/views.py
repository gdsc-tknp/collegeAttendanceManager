from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import UserModelSerializer
from django.contrib.auth import authenticate, login

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_view(request):
    content = {
        'message': 'Hello, World!'
    }
    return Response(content)

@api_view(['POST'])
def signup(request):
    serializer = UserModelSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        content = {
        'message': 'User created successfully'}

        login(request, user)

        return Response(content, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
