from rest_framework import serializers
from .models import Log

class LogSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Log
        fields = '__all__'
