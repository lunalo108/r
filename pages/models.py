from django.db import models
from django.contrib.auth import get_user_model
# User=get_user_model()

class Post(models.Model):
  """This model for post in our blog"""
  title = models.CharField(max_length=120)
  text = models.TextField()
  def __str__(self):
    return self.title

class Comment(models.Model):
  """This model for comment in our posts in blog"""
  text = models.TextField()
  post=models.ForeignKey(
    Post,
    on_delete=models.CASCADE
  )
  def __str__(self):
    return self.text


class Car(models.Model):
  """This model for auth"""
  vin = models.CharField(db_index=True, unique=True, max_length=120)
  brand = models.CharField(max_length=120)
  CAR_TYPES = (
    (1,'Sedan'),
    (2, 'Universal')
  )
  car_type = models.IntegerField(choices=CAR_TYPES)
  # user = models.ForeignKey(User, on_delete=models.CASCADE)