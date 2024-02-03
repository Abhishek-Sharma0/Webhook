from rest_framework import serializers
from .models import Webhook

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Webhook
        fields=('company_id','url','created_at','updated_at','is_active')