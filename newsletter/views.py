from .models import Newsletter
from .serializers import NewsletterSerializer 
from rest_framework import generics

# Create your views here.
class ApiNewsletterPost(generics.ListCreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer