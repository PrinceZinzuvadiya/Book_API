from rest_framework import serializers
from .models import books

class bookserializer(serializers.ModelSerializer):
    class Meta:
        model=books
        fields='__all__'
        