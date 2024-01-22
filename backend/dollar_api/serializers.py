from rest_framework import serializers
from dollar_api.models import Dollar

class DollarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dollar
        fields = [
            'date',
            'source',
            'value_sell',
            'value_buy',
        ]