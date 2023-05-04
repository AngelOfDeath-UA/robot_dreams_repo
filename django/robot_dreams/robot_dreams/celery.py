from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robot_dreams.settings')


app = Celery('robot_dreams')

app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.broker_url = 'amqp:guest@172.17.0.2:5672'

app.autodiscover_tasks()

beat_schedule_sec = 20
app.conf.beat_schedule = {
    'my_schedule': {
        'task': 'user.tasks.delay_task',
        'schedule': beat_schedule_sec,

        'args': (),
        'kwargs': {'sec': beat_schedule_sec}
    }
}