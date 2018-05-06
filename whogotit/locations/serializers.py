from rest_framework import serializers

from models import Location
from profiles.models import UserProfile

class LocationSerializer(serializers.ModelSerializer):
    #username = serializers.SlugRelatedField(slug_field='owner.username',read_only='True')
    #username = serializers.CharField(source='user.username',read_only=True)
    categories = serializers.StringRelatedField(many=True)
    class Meta:
        model = Location
        fields = ('id','name', 'coords','user','username','categories')