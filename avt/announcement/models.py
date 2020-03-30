from django.db import models


# python manage.py makemigrations file
# python manage.py migrate
class Announcement(models.Model):
    id_user = models.CharField(max_length=128)
    description = models.CharField(max_length=300)
    data = models.DateTimeField(auto_now_add="True", auto_now=False)


    # def __str__(self):
    #     return '%s %s' % (self.id, self.login)
    #
    # class Meta:
    #     verbose_name = 'Added announcements'
    #     verbose_name_plural = 'Announcement'
