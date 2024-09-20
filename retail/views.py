from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from retail.models import Chain
from retail.permissions import IsActiveUser
from retail.serializers import ChainSerializer


class ChainViewSet(viewsets.ModelViewSet):
    """API for chain"""
    queryset = Chain.objects.all()
    serializer_class = ChainSerializer
    permission_classes = [IsActiveUser]
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        queryset = super().get_queryset()
        country = self.request.query_params.get('contacts__country')
        if country:
            queryset = queryset.filter(contacts__country=country)
        return queryset
