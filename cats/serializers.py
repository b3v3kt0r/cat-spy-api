from rest_framework import serializers

from cats.models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ["id", "name", "years_of_experience", "breed", "salary"]
