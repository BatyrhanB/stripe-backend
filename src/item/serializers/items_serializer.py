from rest_framework import serializers

from item.models import Item


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "description", "price", "created_at", "updated_at"]
