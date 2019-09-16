# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View

from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Books

# Create your views here.


# class Another(View):

#     books = Book.objects.filter(isPublished = True)
#     print(books)
#     output = ''
#     for book in books:
#         output += f"We have {book.title} books in DB with id = {book.id}<br>"
#     def get(self, request):
#         return HttpResponse(self.output)

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


# def first(request):
#     books = Book.objects.all()
#     return render(request, "first_temp.html",{'books': books})
