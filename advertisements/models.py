from django.db import models

from users.models import User


#ADVERT:
"""
Sender
Post date
if active
City
Phone number
picture
Category
Descripiton

"""


class Category(models.Model):
    name = models.CharField(max_length=128)


class Advert(models.Model):
    title = models.CharField(max_length=128)
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    city = models.CharField(max_length=128)
    phone = models.IntegerField()
    picture = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()









