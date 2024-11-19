from django.urls import path, include
from rest_framework import routers

from missions.views import MissionViewSet


app_name = "missions"

router = routers.DefaultRouter()
router.register("missions", MissionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
