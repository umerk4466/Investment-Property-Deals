from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
  USER_TYPE_CHOICES = (
      (1, 'investor'),
      (2, 'deal_sourcer'),
      (3, 'admin'),
  )

  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,  blank=True, null=True)
# https://github.com/pydanny/multiple-user-types-django/blob/master/spybook/users/models.py


class Investor(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

class Deal_Sourcer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

class Admin(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)