from django.urls import path, include
from rest_framework import routers

from missions.views import MissionViewSet, TargetViewSet


app_name = "missions"

router = routers.DefaultRouter()
router.register("missions", MissionViewSet)
router.register("targets", TargetViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
