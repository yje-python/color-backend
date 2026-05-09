from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import LikedColor, SavedPalette
from .serializers import (
    LikedColorSerializer,
    SavedPaletteSerializer,
)


@api_view(['GET'])
def liked_colors(request):

    colors = LikedColor.objects.all()

    serializer = LikedColorSerializer(colors, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def like_color(request):

    serializer = LikedColorSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['GET'])
def saved_palettes(request):

    palettes = SavedPalette.objects.all()

    serializer = SavedPaletteSerializer(
        palettes,
        many=True
    )

    return Response(serializer.data)


@api_view(['POST'])
def save_palette(request):

    serializer = SavedPaletteSerializer(
        data=request.data
    )

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['DELETE'])
def unlike_color(request):

    user = request.data.get('user')
    hex_code = request.data.get('hex_code')

    liked = get_object_or_404(
        LikedColor,
        user=user,
        hex_code=hex_code
    )

    liked.delete()

    return Response({
        'message': 'deleted'
    })

@api_view(['DELETE'])
def delete_palette(request):

    user = request.data.get('user')
    colors = request.data.get('colors')

    palette = get_object_or_404(
        SavedPalette,
        user=user,
        colors=colors
    )

    palette.delete()

    return Response({
        'message': 'deleted'
    })