from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class LoginUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    password = serializers.CharField(max_length=128, write_only=True, style={'input_type': 'password'})
    
    class Meta:
         model = User
         fields = ['username', 'password', 'access', 'refresh']

    def validate(self, data):
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        print(user, "user")
        try:
            if user is not None: 
                refresh = RefreshToken.for_user(user)
                refresh_token = str(refresh)
                access_token = str(refresh.access_token)
                print("refresh", refresh)
                res = {
                    'email': user.email,
                    'access': access_token,
                    'refresh': refresh_token,
                    'username': username,
                }
                return res
            else:
                raise serializers.ValidationError("Invalid login credentials!")
            
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exists!")


   
class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'})
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs={
            'password2':{'write_only':True}
        }
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError('Password and Confirm Password does not match.')
        return super().validate(attrs)
    
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user