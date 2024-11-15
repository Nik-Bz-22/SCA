from rest_framework import viewsets, status
from .models import Cat, Mission, Target
from .serializers import SpyCatSerializer, MissionSerializer, TargetSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = SpyCatSerializer

class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    @action(detail=True, methods=['post'])
    def assign_cat(self, request, pk=None):
        mission = self.get_object()
        cat_id = request.data.get('cat_id')
        mission.cat = Cat.objects.get(id=cat_id)
        mission.save()
        return Response({'status': 'cat assigned'})

    @action(detail=True, methods=['post'])
    def mark_complete(self, request, pk=None):
        mission = self.get_object()
        mission.is_complete = True
        mission.save()
        return Response({'status': 'mission completed'})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.cat is not None:
            return Response(
                {"detail": "Mission cannot be deleted because it is already assigned to a cat."},
                status=status.HTTP_400_BAD_REQUEST
            )

        self.perform_destroy(instance)
        return Response({"detail": "Mission deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

    @action(detail=True, methods=['post'])
    def mark_complete(self, request, pk=None):
        target = self.get_object()
        target.is_complete = True
        target.save()
        return Response({'status': 'target completed'})


