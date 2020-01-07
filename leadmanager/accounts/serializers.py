from rest_framework import serializers 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate



# Register Serializer 
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id','username','email', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'], email=validated_data['email'])
        return user

# User Serializer 
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User 
        fields = ('id','username', 'email')

# Login Serializer 
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type':'password'}, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user 
        raise serializers.ValidationError("Incorrect Credentials")