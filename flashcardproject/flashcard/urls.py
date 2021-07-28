from . import views
from django.urls import path


urlpatterns = [
    path('flashcard/post_flashcard', views.FlashcardPost.as_view()),
    path('flashcard/<int:flashcard_id>/', views.FlashcardUpdate.as_view()),
    path('collections/<int:collection_id>/', views.FlashcardList.as_view()),
]
