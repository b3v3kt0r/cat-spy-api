from rest_framework import serializers

from missions.models import Mission, Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ["id", "name", "country", "notes", "is_complete"]


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ["id", "cat", "is_complete", "targets"]

    def validate_targets(self, targets):
        if len(targets) < 1 or len(targets) > 3:
            raise serializers.ValidationError("A mission must have 1-3 targets")
        return targets

    def create(self, validated_data):
        targets_data = validated_data.pop("targets")
        mission = Mission.objects.create(**validated_data)

        for target_data in targets_data:
            target = Target.objects.create(**target_data)
            mission.targets.add(target)

        return mission
