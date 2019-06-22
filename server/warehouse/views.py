from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated 
from datetime import datetime

from .models import Item, Log
from .serializers import ItemSerializer, ItemListSerializer, LogSerializer

class ItemListView(APIView):
	permission_classes = (IsAuthenticated,)
	
	def get(self, request, format=None):
		items = Item.objects.order_by('name')
		serializer = ItemListSerializer(items, many=True)

		return Response(serializer.data)


class ItemDetailView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, pk, format=None):
		item = get_object_or_404(Item, pk=pk)
		serializer = ItemSerializer(item)

		return Response(serializer.data)


class ItemReservationView(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request, format=None):
		item = get_object_or_404(Item, request.data['pk'])
		if item.state == 1:
			validated_data = {
				'user':UserModel,
				'state':'Rezervuota',
				'date':datetime.now()
				}
			serializer = ItemSerializer().update(item, validated_data)
		


class LogView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, pk, format=None):
		log = get_object_or_404(Log, pk=pk)
		serializer = LogSerializer(log)

		return Response(serializer.data)
