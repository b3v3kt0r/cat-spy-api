from rest_framework import serializers

from missions.models import Mission, Target


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ["id", "name", "cats", "status", "targets", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ["id", "name", "country", "notes", "status"]
