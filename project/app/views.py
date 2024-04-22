from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import Regist_Serializer
from .models import RegistrationModel
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.

class SnippetList(APIView):
    def get(self, request, format=None):
        snippets = RegistrationModel.objects.all()
        serializer = Regist_Serializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Regist_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res=("data successfully created")
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return Response("data created", status=status.HTTP_201_CREATED)
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SnippetDetail(APIView):
    def get_object(self, pk):
        try:
            return RegistrationModel.objects.get(pk=pk)
        except RegistrationModel.DoesNotExist:
             raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Regist_Serializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Regist_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)