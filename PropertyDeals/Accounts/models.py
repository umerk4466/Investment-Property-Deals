from django.contrib.auth.models import AbstractUser
from django.db import models

# Define models here.
class User(AbstractUser):
  USER_TYPE_CHOICES = (
      (1, 'Investor'),
      (2, 'Deal sourcer'),
      (3, 'Admin'),
      (4, 'Super admin'),
  )

  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,  default=USER_TYPE_CHOICES[0][0])
# https://github.com/pydanny/multiple-user-types-django/blob/master/spybook/users/models.py

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(blank=True)
  picture = models.ImageField(
        upload_to='profile_images', blank=True, null=True)
  phone_number = models.CharField(max_length=30, blank=True)
  display_name = models.CharField(max_length=255, blank=True)
  date_of_birth = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
  country = models.CharField(max_length=255, blank=True)
  city = models.CharField(max_length=255, blank=True)

  GENDER_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
    )
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

  def __str__(self):
    return self.user.username

class Investor(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  post_code = models.CharField(max_length=255)
  # preferred_investment = 


class DealSourcer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  post_code = models.CharField(max_length=255)
  specialized_in = models.CharField(max_length=255, blank=True)
  

# class DealSourcerCompany():
#   deal_sourcer = models.OneToOneField(User, on_delete=models.CASCADE)
#   name = 
#   website = 
#   phone_number =
#   email = 
#   post_code = 



class Admin(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)