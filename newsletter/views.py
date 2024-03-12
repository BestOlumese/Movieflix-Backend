from rest_framework.response import Response
from .models import Newsletter
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from .serializers import NewsletterSerializer 
from rest_framework import status

# Create your views here.
@csrf_exempt
class ApiNewsletterPost(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data
        newsletter = Newsletter.objects.create(email["email"])
        newsletter.save()
        serializer = NewsletterSerializer(newsletter)
        return Response(serializer.data)