from celery.schedules import crontab

from celery import Celery

app = Celery('school', broker='redis://localhost:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')


@app.task
def print_hello_world():
    print("Hello, World!")


app.conf.beat_schedule = {
    'print-hello-world-every-minute': {
        'task': 'school.tasks.print_hello_world',
        'schedule': crontab(minute="*/1"),
    },
}
