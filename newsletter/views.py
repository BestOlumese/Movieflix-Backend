from rest_framework.response import Response
from .models import Newsletter
from rest_framework.generics import CreateAPIView
from django.views.decorators.csrf import csrf_exempt
from .serializers import NewsletterSerializer 
from rest_framework import status

# Create your views here.
@csrf_exempt
class ApiNewsletterPost(CreateAPIView):
    def post(self, request, format=None):
        serializer = NewsletterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)