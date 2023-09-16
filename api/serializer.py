from rest_framework import serializers

from .models import (
                    MyUser,
                    Profile    
                )

class RegistrationSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()

    