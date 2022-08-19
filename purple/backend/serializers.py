from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Curation, Place, Location, Category, Purpose1, Purpose2

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username']

class CurationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Curation
        fields = ['user', 'id', 'image', 'title', 'content', 'created_at']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Purpose1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose1
        fields = '__all__'

class Purpose2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose2
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    loc = LocationSerializer(read_only=True)
    cat = CategorySerializer(read_only=True)
    pur1 = Purpose1Serializer(read_only=True)
    pur2 = Purpose2Serializer(read_only=True)    
    class Meta:
        model = Place
        fields = '__all__'