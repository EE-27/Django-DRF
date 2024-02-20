from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from tracker.models import Habit
from tracker.paginators import HabitPagination
from tracker.permissions import IsOwner
from tracker.serializers import HabitSerializer


class HabitCreateApiView(generics.CreateAPIView):
    """
    Create new Habit.
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitListApiView(generics.ListAPIView):
    """
    List of all Habits
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPagination

    def get_queryset(self):
        return Habit.objects.filter(public=True)


class HabitRetrieveApiView(generics.RetrieveAPIView):
    """
    Show one Habit.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitUpdateApiView(generics.UpdateAPIView):
    """
    Update Habit.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitDestroyApiView(generics.DestroyAPIView):
    """
    Delete Habit.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class UserHabitListApiView(generics.ListAPIView):
    """
    List of Habits owned by the User.
    """
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)
