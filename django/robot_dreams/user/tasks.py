from celery import shared_task
from .models import User
from purchase.models import Purchase


@shared_task
def my_task():
    print('Helle World from Celery!')

@shared_task(bind=False)
def count_purchase(user_id):
    count_purchase = Purchase.objects.filter(user_id=user_id).count()
    print(f'User_id {user_id} - have {count_purchase} purchases.')


@shared_task(bind=False)
def delay_task(sec):
    count_all_user = User.objects.count()
    print(f'Delay task DONED per {sec} sec.\n'
          f'In DataBase {count_all_user} users.')
