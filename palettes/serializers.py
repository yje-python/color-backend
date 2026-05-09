from rest_framework import serializers
from .models import LikedColor, SavedPalette


class LikedColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = LikedColor
        fields = '__all__'


class SavedPaletteSerializer(serializers.ModelSerializer):

    class Meta:
        model = SavedPalette
        fields = '__all__'