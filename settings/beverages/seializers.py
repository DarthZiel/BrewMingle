from rest_framework.serializers import ModelSerializer
from .models import Coffee, Step


class StepSerializer(ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'


class CoffeeSerializer(ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Coffee
        fields = ['id', 'name', 'description', 'image', 'steps']

