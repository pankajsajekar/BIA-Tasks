from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BookSerializer
from .models import Book
from rest_framework import status
from rest_framework import generics

# Using Class Base View 
class BookAddView(APIView):
    serializer_class = BookSerializer
    model_class = Book

    def post(self, request):
        jsonData = request.data
        serializer = self.serializer_class(data=jsonData)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            status_code = status.HTTP_201_CREATED
            res = {
                "success" : True,
                "message" : "New Book Added!",
                "statusCode" : status_code,
                "data" : serializer.data,
            }
            return Response(res, status=status_code)
        

# using Generics method
class BookRetriveView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    
class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
