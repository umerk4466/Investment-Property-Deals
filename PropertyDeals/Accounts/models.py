from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
  USER_TYPE_CHOICES = (
      (1, 'investor'),
      (2, 'deal_sourcer'),
  )

  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,  blank=True, null=True)