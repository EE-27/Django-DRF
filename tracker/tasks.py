from celery import Celery

from tracker.models import Habit
from users.models import User

app = Celery('tracker', broker='redis://localhost:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')

from django.utils import timezone


def send_notification(user_id, habit_id):
    now = timezone.now()
    current_time = now.strftime("%H:%M:00")
    current_date = now.date()

    user = User.objects.get(id=user_id)
    habit = Habit.objects.get(id=habit_id)

    current_period = (current_date - habit.initial_date).days

    if current_period % habit.periodicity == 0:
        if current_time == habit.time.strftime('%H:%M:00'):
            message = f"{user.first_name}, it's time to {habit.habit_name}. You should go {habit.activity} for {habit.time_to_complete} minutes."
            print(message)


@app.task
def schedule_habit_notifications():
    habits_to_notify = Habit.objects.all()

    for habit in habits_to_notify:
        send_notification(habit.user.id, habit.id)
