from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics.ListAPIView
from rest_framework.viewsets.ModelViewSet
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    """
    A ViewSet for performing CRUD operations on the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users