from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics.ListAPIView
from rest_framework.viewsets.ModelViewSet

from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
