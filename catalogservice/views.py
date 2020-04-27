from django.shortcuts import render
from rest_framework import viewsets
from catalogservice import models as app_models
from catalogservice import serializers

class CatalogViewSet(viewsets.ModelViewSet):
    queryset = app_models.CatalogItem.objects.all()
    serializer_class = serializers.CatalogItemSerializer
