from rest_framework_gis import serializers
from rest_framework import serializers as serial
from .models import farm, farmer, partner

#farms
class farmSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = farm
        fields = ("id","grower_id","area")
        geo_field = "geom"
        
class farmerSerializer(serial.ModelSerializer):
    class Meta:
        model = farmer
        fields = '__all__'

class partnerSerializer(serial.ModelSerializer):
    class Meta:
        model = partner
        fields = '__all__'