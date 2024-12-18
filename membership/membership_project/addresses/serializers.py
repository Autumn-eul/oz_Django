from rest_framework.serializers import ModelSerializer
from .models import Address

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "user", "street", "city", "state", "postal_code", "country"]