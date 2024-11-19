from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from missions.models import Mission, Target
from missions.serializers import MissionSerializer


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()

        if mission.cat:
            return Response(
                "You can't delete mission already assigned to a cat!",
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().destroy(request, *args, **kwargs)

    @action(detail=True, methods=["PATCH"])
    def assign_cat(self, request, pk=None):
        mission = self.get_object()
        cat_id = request.data.get("cat_id")

        if Mission.objects.filter(Q(cat_id=cat_id) & Q(is_complete=False)).exists():
            return Response(
                "Cat already has a mission", status=status.HTTP_400_BAD_REQUEST
            )

        mission.cat_id = cat_id
        mission.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=["PATCH"])
    def update_notes(self, request, pk=None):
        mission = self.get_object()
        notes = request.data.get("notes")
        target_id = request.data.get("target_id")

        try:
            target = mission.targets.get(id=target_id)
        except Target.DoesNotExist:
            return Response(
                {"error": "Target not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if mission.is_complete or target.is_complete:
            return Response(
                "You can't update notes when mission or target is complete",
                status=status.HTTP_400_BAD_REQUEST,
            )

        target.notes = notes
        target.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=["PATCH"])
    def complete_mission(self, request, pk=None):
        mission = self.get_object()

        target = mission.targets.first()

        if not target or not target.is_complete:
            return Response(
                {"error": "Target must be completed before mission closure"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        mission.is_complete = True
        mission.save()

        return Response(self.get_serializer(mission).data)
