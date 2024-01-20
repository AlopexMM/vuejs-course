from django.forms.models import model_to_dict
from dollar_api.models import Dollar
from dollar_api.serializers import DollarSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    instance = Dollar.objects.all().order_by('?').first()
    data = {}
    if instance:
        data = DollarSerializer(instance).data
    return Response(data)