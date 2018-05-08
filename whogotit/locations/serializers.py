from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from models import Location,Category
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('name', 'desc',)

class LocationSerializer(serializers.ModelSerializer):
    #username = serializers.SlugRelatedField(slug_field='owner.username',read_only='True')
    #username = serializers.CharField(source='user.username',read_only=True)
    #categories = serializers.StringRelatedField(many=True)
    #categories = CategorySerializer(many=True)
    class Meta:
        model = Location
        fields = ('id','name', 'coords','owner','username','categories')
    # def create(self, validated_data):
    #     categories_data = validated_data.pop('categories')
    #     print categories_data
    #     location = Location.objects.create(**validated_data)
    #     location.save()
    #     # for category_data in categories_data:
    #     #     location.categories.add(**category_data)
    #     return location
    
class ListLocationSerializer(serializers.ModelSerializer):
    
    categories = serializers.StringRelatedField(many=True)
    categories = CategorySerializer(many=True)
    class Meta:
        model = Location
        fields = ('id','name', 'coords','owner','username','categories')
   
        
