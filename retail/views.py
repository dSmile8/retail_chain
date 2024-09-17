from rest_framework import viewsets

from retail.models import Chain
from retail.permissions import IsActiveUser
from retail.serializers import ChainSerializer


class ChainViewSet(viewsets.ModelViewSet):
    queryset = Chain.objects.all()
    serializer_class = ChainSerializer
    permission_classes = [IsActiveUser]
