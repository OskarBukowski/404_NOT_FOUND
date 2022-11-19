from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Advert(models.Model):
    title = models.CharField(max_length=128)
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    city = models.CharField(max_length=128)
    phone = models.IntegerField()
    picture = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title


class Image(models.Model):
    imagefile = models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return str(self.imagefile)
