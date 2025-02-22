from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
# Create your views here.
from .serializers import NotificationSerializer
from rest_framework.pagination import PageNumberPagination
from .models import FollowNotification
from django.db import transaction

class NotificationPagination(PageNumberPagination):
    page_size = 5
    ordering = "-created_at"

class ListNotificationView(ListAPIView):
    serializer_class = NotificationSerializer
    pagination_class = NotificationPagination


    def get_queryset(self):
        id = self.kwargs['id']
        queryset = FollowNotification.objects.select_related("user").filter(user_id = id)
        # queryset = FollowNotification.objects.all()
        return queryset
    
    def list(self, request, *args, **kwargs):
        res = super().list(request,*args,**kwargs)
        user = request.user
        res.data["read_count"] = FollowNotification.objects.filter(user=user,is_read=False).count()
        return res
    
class ClearNotification(APIView):
    def put(self,request,*args, **kwargs):
        user = request.user
        with transaction.atomic():
            FollowNotification.objects.filter(user=user).update(is_read=True)
        return Response({"message": 'cleared all notification'})
