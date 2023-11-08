from rest_framework import serializers
from .models import Restaurant
from datetime import datetime, time

class RestaurantSerializer(serializers.ModelSerializer):
    is_open = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'opening_time', 'closing_time','is_open']


    def get_is_open(self, obj):
        now = datetime.now().time()
        return obj.opening_time <= now <= obj.closing_time