from rest_framework.viewsets import ModelViewSet

from .seializers import CoffeeSerializer, StepSerializer

from .models import Coffee, Step
from django.db.models import Prefetch



class CoffeeModelViewSet(ModelViewSet):
    queryset = Coffee.objects.prefetch_related(
        Prefetch('steps', queryset=Step.objects.order_by('step_number'))
    )
    serializer_class = CoffeeSerializer
    ordering_fields = ('steps__step_number',)

