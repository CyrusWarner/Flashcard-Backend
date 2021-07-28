
from django.http import Http404
from .models import CollectionOfFlashCards
from .serializers import CollectionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.apps import apps
from django.db.models import Q


class CollectionList(APIView):

    def get(self, request):
        collection = CollectionOfFlashCards.objects.all()
        serializer = CollectionSerializer(collection, many=True)
        return Response(serializer.data)




