from django.forms.models import model_to_dict
from dollar_api.models import Dollar
from dollar_api.serializers import DollarSerializer

from rest_framework.generics import ListAPIView
from django.http import Http404

import datetime

"""
This has the view for:
One specific day, month, year, and you can get all
"""

class DollarList(ListAPIView):
    """
    Get all dollar exchange rate for oficial and blue
    and search for params if there is any
    """
    serializer_class = DollarSerializer

    def get_queryset(self):
        queryset = Dollar.objects.all()
        source = self.request.query_params.get('source')
        date = self.request.query_params.get('date')
        if source is not None and date is not None:
            date = datetime.date.fromisoformat(date)
            queryset = queryset.filter(date=date, source=source)
        elif source is not None:
            queryset = queryset.filter(source=source)
        elif date is not None:
            date = datetime.date.fromisoformat(date)
            queryset = queryset.filter(date=date)
        return queryset

dollar_list_all = DollarList.as_view()