from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

@api_view(['POST'])
def signup(request):

    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response(
            {'error': 'already exists'},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(
        username=username,
        password=password
    )

    return Response({
        'id': user.id,
        'username': user.username,
    })

@api_view(['POST'])
def login(request):

    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(
        username=username,
        password=password
    )

    if user is None:

        return Response(
            {'error': 'invalid'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    return Response({
        'id': user.id,
        'username': user.username,
    })