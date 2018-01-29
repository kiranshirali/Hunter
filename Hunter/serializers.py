from rest_framework import serializers

from .models import HttpEndpoint



class HttpEndpointSerializer(serializers.ModelSerializer):
    """
    Serializing all the Authors
    """
    class Meta:
        model = HttpEndpoint
        fields = '__all__'