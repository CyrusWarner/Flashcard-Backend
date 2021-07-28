from . import views
from django.urls import path


urlpatterns = [
    path('collections/', views.CollectionList.as_view()),
]
