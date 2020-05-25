from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers


class CreateUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'token',
        )
        read_only_fields = ('token',)

    def create(self, validated_data):
        if validated_data.get('password1') == validated_data.get('password2'):
            validated_data['password'] = validated_data.get('password1')
            validated_data.pop('password1', None)
            validated_data.pop('password2', None)
            user = super(CreateUserSerializer, self).create(validated_data)
            user.set_password(validated_data['password'])
            user.save()
            token = Token.objects.get_or_create(user=user)
            user.token = token[0].key
            return user
        return User.objects.none()


class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email'
        )
