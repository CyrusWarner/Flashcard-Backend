from . import views
from django.urls import path


urlpatterns = [
    path('flashcard/<int:flashcard_id>/', views.FlashCardUpdate.as_view()),
    path('collections/<int:collection_id>/', views.FlashcardList.as_view()),
]
