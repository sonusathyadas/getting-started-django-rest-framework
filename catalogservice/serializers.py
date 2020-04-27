
from rest_framework import serializers
from catalogservice import models as app_models

class CatalogItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = app_models.CatalogItem
        fields = "__all__"