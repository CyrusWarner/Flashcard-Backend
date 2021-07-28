from django.db import models


class Flashcard(models.Model):
    collection = models.ForeignKey('collectionofflashcards.CollectionOfFlashCards', on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=500)
