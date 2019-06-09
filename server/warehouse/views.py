from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Item
from .serializers import ItemSerializer, ItemListSerializer

class ItemListView(APIView):

	def get(self, request, format=None):
		items = Item.objects.order_by('name')
		serializer = ItemListSerializer(items, many=True)

		return Response(serializer.data)


class ItemDetailView(APIView):

    def get(self, request, pk, format=None):
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemSerializer(item)

        return Response(serializer.data)