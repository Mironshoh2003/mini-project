from django.shortcuts import render
from books.models import Book
from rest_framework.generics import ListAPIView
from .serializers import BookSerializers


class BookApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
