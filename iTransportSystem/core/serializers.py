from rest_framework.serializers import ModelSerializer
from .models import Transport


class TransportSerializer(ModelSerializer):
    class Meta:
        model = Transport
        fields = "__all__"
