from rest_framework import viewsets, status
from rest_framework.response import Response

from cats.models import Cat
from cats.serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        allowed_updates = {'salary'}
        if any(key not in allowed_updates for key in request.data.keys()):
            return Response(
                {"error": "Only salary can be updated"},
                status=status.HTTP_400_BAD_REQUEST
            )

        self.perform_update(serializer)
        return Response(serializer.data)
