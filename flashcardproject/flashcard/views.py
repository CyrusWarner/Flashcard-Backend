
from django.http import Http404
from .models import Flashcard
from .serializers import FlashcardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.apps import apps
from django.db.models import Q

# Create your views here.


class FlashcardList(APIView):
    def get(self, request, collection_id):
        flashcards = Flashcard.objects.filter(collection_id=collection_id)
        serializer = FlashcardSerializer(flashcards, many=True)
        return Response(serializer.data)

