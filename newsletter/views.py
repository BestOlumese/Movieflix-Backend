from .models import Newsletter
from django.views.decorators.csrf import csrf_exempt
from .serializers import NewsletterSerializer 
from rest_framework import generics

# Create your views here.
@csrf_exempt
class ApiNewsletterPost(generics.CreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer