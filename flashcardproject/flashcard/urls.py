from . import views
from django.urls import path


urlpatterns = [
    path('collections/<int:collection_id>/', views.FlashcardList.as_view()),
]

# path('collections/', views.CollectionList.as_view()),
