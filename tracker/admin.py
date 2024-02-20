from django.contrib import admin

from tracker.models import Habit


# Register your models here.

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("user", "activity")
