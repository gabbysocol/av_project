from django.db import models


# python manage.py makemigrations file
# python manage.py migrate
class User(models.Model):
    login = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    father_name = models.CharField(max_length=45)
    mobile = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=64)
