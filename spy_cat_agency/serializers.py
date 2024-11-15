from rest_framework import serializers
from .models import Cat, Mission, Target
from .cat_validator import validate_breeds

class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ['id', 'name', 'experience', 'breed', 'salary']

    @staticmethod
    def validate_breed(breed):
        if not validate_breeds(breed):
            raise serializers.ValidationError(f"The breed '{breed}' is not valid according to the API.")
        return breed

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'is_complete']

    def update(self, instance, validated_data):
        mission = instance.get_mission()

        if instance.is_complete:
            raise serializers.ValidationError("Notes cannot be updated because the target is already complete.")

        if mission and mission.is_complete:
            raise serializers.ValidationError("Notes cannot be updated because the mission is already complete.")

        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()
        return instance

class MissionSerializer(serializers.ModelSerializer):
    cat_id = serializers.IntegerField(write_only=True, required=False)
    targets = TargetSerializer(many=True)
    class Meta:
        model = Mission
        fields = ['id', 'cat_id', 'targets', 'is_complete']

    def create(self, validated_data):
        try:
            cat_id = validated_data.pop('cat_id')
            cat = Cat.objects.get(id=cat_id)

        except KeyError:
            cat = None

        targets_info = validated_data.pop('targets')

        mission = Mission.objects.create(cat=cat, is_complete=validated_data["is_complete"])
        for target in targets_info:
            t = Target.objects.create(**target)
            mission.targets.add(t)

        mission.save()
        return mission

