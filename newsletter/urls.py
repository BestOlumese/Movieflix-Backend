from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiNewsletterPost.as_view()),
]