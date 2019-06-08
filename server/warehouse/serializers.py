from rest_framework import serializers
from .models import Item

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        depth = 2
        fields = ('id', 'name', 'category', 'color', 'condition', 'slug')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        depth = 2
        fields = ('id', 'name', 'category', 'color', 'condition', 'description', 'slug')