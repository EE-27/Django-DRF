from rest_framework import serializers

from tracker.models import Habit
from tracker.validators import PlaceValidator, PeriodicityValidator, EnjoyableRewardValidator, TimeToCompleteValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            PlaceValidator(field="place"),
            PeriodicityValidator(field="periodicity"),
            EnjoyableRewardValidator(),
            TimeToCompleteValidator(field="time_to_complete"),
        ]