from django.contrib import admin

from .models import Article


# superuser: admin
# password: admin
admin.site.register(Article)
