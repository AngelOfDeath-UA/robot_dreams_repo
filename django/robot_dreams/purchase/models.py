from django.db import models
from user.models import User
from book.models import Book


class Purchase(models.Model):
    user_id = models.ForeignKey(User, related_name='user_id', on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, related_name='book_id', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)  # Используем auto_now_add для автоматического установления значения

    # при создании новой сущности

    def __str__(self):
        return f'{self.user_id.first_name} | {self.book_id.title} | {self.date}'

    class Meta:
        db_table = 'purchases'
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'
        ordering = ['-date']
