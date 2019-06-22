from rest_framework import serializers
from .models import Item, Log
from django.contrib.auth import get_user_model

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        depth = 2
        fields = ('id', 'name', 'category', 'color', 'condition', 'state', 'slug')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        depth = 2
        fields = (
            'id', 
            'name', 
            'category', 
            'color', 
            'condition', 
            'description', 
            'user', 
            'state', 
            'date', 
            'slug'
            )
        
    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.color = validated_data.get('color', instance.color)
        instance.condition = validated_data.get('condition', instance.condition)
        instance.description = validated_data.get('description', instance.description)
        instance.user = validated_data.get('user', instance.user)
        instance.state = validated_data.get('state', instance.state)
        instance.date = validated_data.get('date', instance.date)

        return instance


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        depth = 2
        fields = ('id', 'action', 'item', 'date', 'user')

    def create(self, validated_data):
        return Log.objects.create(**validated_data)