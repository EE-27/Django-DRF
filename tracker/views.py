from django.shortcuts import render
from rest_framework import viewsets

from tracker.models import Habit
from tracker.paginators import HabitPagination
from tracker.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):

    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    queryset = Habit.objects.all()


