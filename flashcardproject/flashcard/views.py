
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


class FlashcardUpdate(APIView):
    def put(self, request, flashcard_id):
        flashcard = Flashcard.objects.get(pk=flashcard_id)
        serializer = FlashcardSerializer(flashcard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashcardPost(APIView):
    def post(self, request):
        serializer = FlashcardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashcardDelete(APIView):
    def delete(self, request, flashcard_id):
        flashcard = Flashcard.objects.get(pk=flashcard_id)
        flashcard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
