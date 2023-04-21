from django.db import models


class Book(models.Model):

    title = models.CharField(max_length=150, null=False)
    author = models.CharField(max_length=150, null=False)
    year = models.SmallIntegerField()
    price = models.FloatField(max_length=6, null=False)

    def __str__(self):
        return f'{self.title} - {self.author} | {self.year}'

    class Meta:
        db_table = 'book'
        unique_together = [['author', 'title']]
        verbose_name = 'book'
        verbose_name_plural = 'books'
