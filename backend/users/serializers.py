from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
    def validate(self, data):

        """
        Custom validation to ensure non-empty username and password.
        """
        username = data.get('username')
        password = data.get('password')

        # Check if username is empty
        if not username:
            raise serializers.ValidationError("Username cannot be empty.")

        # Check if password is empty
        if not password:
            raise serializers.ValidationError("Password cannot be empty.")

        return data
