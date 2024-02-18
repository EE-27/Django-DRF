from django.db import models

from config import settings


class Habit(models.Model):
    PLACE_CHOICES = [
        ("Indoor", "Indoor"),
        ("Outdoor", "Outdoor")
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")

    place = models.CharField(max_length=12, choices=PLACE_CHOICES, verbose_name="Place")
    time = models.TimeField(verbose_name="Time")

    habit_name = models.CharField(max_length=24, verbose_name="Habit")
    activity = models.CharField(max_length=512, verbose_name="Activity")

    enjoyable = models.BooleanField(default=False, verbose_name="Enjoyable")

    reward = models.BooleanField(default=False, verbose_name="Reward")

    linked_habit = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name='linked_habits', verbose_name="Linked Habit")

    periodicity = models.PositiveSmallIntegerField(verbose_name="Periodicity")
    time_to_complete = models.PositiveIntegerField(verbose_name="Time to complete")
    public = models.BooleanField(default=False, verbose_name="Public")

    def __str__(self):
        return f'I, {self.user}, will {self.habit_name} at {self.time} in {self.place}'

    class Meta:
        ordering = ("pk", )
