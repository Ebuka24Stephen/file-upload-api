from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializers import UploadFileSerializer
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from .models import UploadedFile
from rest_framework.parsers import MultiPartParser, FormParser
class FileViewSet(viewsets.ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadFileSerializer
    parser_classes = (MultiPartParser, FormParser)  

    def create(self, request):
        serializer = UploadFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        file = get_object_or_404(self.queryset, id=pk)
        serializer = self.get_serializer(file, partial=True, data=request.data), 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        file = get_object_or_404(self.queryset, id=pk)
        serializer = self.get_serializer(file)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        file  = get_object_or_404(self.queryset, id=pk)
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
