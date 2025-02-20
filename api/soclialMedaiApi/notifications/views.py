from django.shortcuts import render
from rest_framework.generics import ListAPIView
# Create your views here.
from .serializers import NotificationSerializer
from rest_framework.pagination import PageNumberPagination
from .models import FollowNotification


class NotificationPagination(PageNumberPagination):
    page_size = 5

class ListNotificationView(ListAPIView):
    serializer_class = NotificationSerializer
    pagination_class = NotificationPagination
    lookup_field = 'id'
    queryset = FollowNotification.objects.all()
    

