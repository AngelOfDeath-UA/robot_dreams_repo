from django.db import models
from django.urls import reverse


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=80, null=False)
    age = models.SmallIntegerField(null=False)

    def __str__(self):
        return f'{self.id}: {self.first_name}'

    def get_absolute_url(self):
        return reverse('user', kwargs={"id": self.id})

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
