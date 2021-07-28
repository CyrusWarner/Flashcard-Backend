from rest_framework import serializers
from .models import CollectionOfFlashCards


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionOfFlashCards
        fields = ["id", "name", "description"]
