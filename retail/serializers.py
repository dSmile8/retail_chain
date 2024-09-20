from rest_framework import serializers

from retail.models import Chain


class ChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chain
        exclude = ("debt_to_supplier",)
