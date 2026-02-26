from rest_framework import serializers
from .models import UserProfile, Property, PropertyImage, Review, Favorite

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'role', 'phone_number']

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image']

class PropertyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'title', 'price', 'city', 'property_type', 'rooms']

class PropertyDetailSerializer(serializers.ModelSerializer):
    # Подтягиваем связанные изображения и данные продавца
    images = PropertyImageSerializer(many=True, read_only=True)
    seller = UserProfileSerializer(read_only=True)

    class Meta:
        model = Property
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Review
        fields = ['id', 'author', 'stars', 'comment', 'created_date']