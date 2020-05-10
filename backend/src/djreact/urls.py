from django.contrib import admin
from django.urls import path, include

# python manage.py makemigrations
# python manage.py migrate
# python manage.py migrate --run-syncdb
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('articles.api.urls')),
]
