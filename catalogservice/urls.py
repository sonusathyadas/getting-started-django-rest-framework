from django.urls import path, include
from rest_framework import routers
from catalogservice import views as app_views

router = routers.DefaultRouter()
router.register("", app_views.CatalogViewSet)

urlpatterns=[
    path("", include(router.urls ))
]