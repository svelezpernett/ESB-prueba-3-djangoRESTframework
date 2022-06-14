from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import action
from ESB_api.models import *
from ESB_api.serializers import *

# Create your views here.

class Cliente_viewset(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = Cliente_serializer

    #@action(methods=['get'], detail=True, url_path='get', url_name='change_password')
    def get(self, request):
        self.serializer_class(self.queryset, many=True)
        return Response(self.serializer_class.data)

    def post(self, request, format=None):
        serialized_data_POST = self.serializer_class(data=request.data)
        if serialized_data_POST.is_valid():
            serialized_data_POST.save()
            return Response(serialized_data_POST.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data_POST.errors, status=status.HTTP_400_BAD_REQUEST)