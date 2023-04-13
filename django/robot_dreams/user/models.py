from django.db import models

# Create your models here.
class User(models.Model):

    first_name = models.CharField(max_length=80, null=False)
    age = models.SmallIntegerField(null=False)

    def __str__(self):
        return str(self.first_name)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
