from django.urls import path, include
from rest_framework import routers

from cats.views import CatViewSet


app_name = "cats"

router = routers.DefaultRouter()
router.register("cats", CatViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
