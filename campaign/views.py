# campaign/views.py

from rest_framework import viewsets
from .models import Campaign
from .serializers import CampaignSerializer
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum
class CampaignViewSet(ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    
class CampaignDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = (AllowAny,)

class CampaignStatsAPIView(APIView):  # Add this new view
    permission_classes = (AllowAny,)  # Adjust permissions as needed

    def get(self, request):
        total_campaigns = Campaign.objects.count()
        total_revenue = Campaign.objects.aggregate(Sum('expected_revenue'))['expected_revenue__sum'] or 0
        total_actual_cost = Campaign.objects.aggregate(Sum('actual_cost'))['actual_cost__sum'] or 0

        return Response({
            'total_campaigns': total_campaigns,
            'total_revenue': str(total_revenue),  # Convert to string if needed
            'total_actual_cost': str(total_actual_cost),  # Convert to string if needed
        })
