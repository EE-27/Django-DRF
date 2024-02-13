from rest_framework import serializers

from tracker.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    model = Habit
    fields = "__all__"
