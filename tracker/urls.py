from django.urls import path

from tracker.apps import TrackerConfig
from tracker.views import HabitCreateApiView, HabitListApiView, HabitRetrieveApiView, HabitUpdateApiView, \
    HabitDestroyApiView, UserHabitListApiView

app_name = TrackerConfig.name

urlpatterns = [
    path("habits/create/", HabitCreateApiView.as_view(), name="create-habit"),
    path("habits/", HabitListApiView.as_view(), name="habits-list"),
    path("habits/<int:pk>/", HabitRetrieveApiView.as_view(), name="retrieve-habit"),
    path("habits/update/<int:pk>/", HabitUpdateApiView.as_view(), name="update-habit"),
    path("habits/delete/<int:pk>/", HabitDestroyApiView.as_view(), name="delete-habit"),

    path("user_habits/", UserHabitListApiView.as_view(), name="user-habits")
]
