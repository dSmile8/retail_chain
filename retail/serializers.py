from rest_framework import serializers

from retail.models import Chain


class ChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chain
        # fields = ('name', 'contacts', 'products', 'parent', 'created_at')
        # fields = '__all__'
        exclude = ("debt_to_supplier",)