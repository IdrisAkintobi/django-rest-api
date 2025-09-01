from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "first_name", "last_name", "password"]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def validate_password(self, value):
        """Use Django’s built-in password validators"""
        try:
            validate_password(value)
        except DjangoValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']

        user = get_user_model().objects.create(email=email, username=username, first_name=first_name, last_name=last_name)
        user.set_password(validated_data["password"])
        user.save()
        return user

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["email", "username", "first_name", "last_name", "bio", "profile_picture", "facebook", "linkedin"]
        # make username optional
        extra_kwargs = {
            "username": {
                "required": False
            }
        }