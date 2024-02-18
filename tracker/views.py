from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from tracker.models import Habit
from tracker.paginators import HabitPagination
from tracker.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):

    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [AllowAny]
    queryset = Habit.objects.all()


