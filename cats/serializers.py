from rest_framework import serializers
import requests

from cats.models import Cat


class BreedValidationService:
    @staticmethod
    def validate_breed(breed):
        try:
            response = requests.get(
                "https://api.thecatapi.com/v1/breeds/search", params={"q": breed}
            )
            return len(response.json()) > 0
        except Exception:
            return False


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ["id", "name", "years_of_experience", "breed", "salary"]

    def validate_breed(self, value):
        if not BreedValidationService.validate_breed(value):
            raise serializers.ValidationError("Invalid cat breed")
        return value
