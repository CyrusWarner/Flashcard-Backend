from django.db import models


class Flashcard(models.Model):
    collection = models.ForeignKey('collectionofflashcards.CollectionOfFlashCards', on_delete=models.CASCADE)
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=150)
