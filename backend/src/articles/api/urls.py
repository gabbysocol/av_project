from django.urls import path, include

from .views import ArticleListView, ArticleDetalView


urlpatterns = [
    path('', ArticleListView.as_view()),
    path('<pk>', ArticleDetalView.as_view())
]
