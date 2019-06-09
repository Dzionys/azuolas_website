from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.http import JsonResponse

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create(
            username=validated_data['username'],
            phone=validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()

        return user

    def login_check(self):
        if not UserModel.is_active :
            return JsonResponse({'error':'vartotojas neaktyvuotas'}, status=400)
        else:
            return JsonResponse({'ok':True}, status=200)

    class Meta:
        model = UserModel
        fields = ('username', 'password', 'phone')