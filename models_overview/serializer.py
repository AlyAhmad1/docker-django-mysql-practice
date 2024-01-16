from rest_framework import serializers
from .models import Place, Restaurant


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
        extra_kwargs = {'name': {'validators': []}}


class RestaurantSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()

    class Meta:
        model = Restaurant
        fields = '__all__'

    def create(self, validated_data):
        place_data = validated_data.pop('place')
        place_name = place_data.get('name')

        # Check if a Place with the same name already exists
        place_instance, created = Place.objects.get_or_create(name=place_name)

        # If the Place was not created in this step, it already existed
        if not created:
            # Use the existing Place instance
            validated_data['place'] = place_instance
        else:
            # Create a new Place instance
            validated_data['place'] = Place.objects.create(**place_data)

        restaurant = Restaurant.objects.create(**validated_data)
        return restaurant

