from .models import Place, Restaurant
from .serializer import PlaceSerializer, RestaurantSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class PlaceList(APIView):

    # permission_classes = [IsAuthenticated]

    def get(self, request):
        places_data = Place.objects.all()
        serializer = PlaceSerializer(places_data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            place_name = serializer.validated_data.get('name')

            # Check if a Place with the same name already exists
            existing_place = Place.objects.filter(name=place_name).first()

            if existing_place:
                # If the Place already exists, return the existing Place ID
                response_data = {'message': 'Place already exists', 'place_id': existing_place.uuid}
                return Response(response_data, status=status.HTTP_200_OK)

            # Continue with the creation process if no validation issues
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantList(APIView):
    def get(self, request):
        restaurant_data = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurant_data, many=True).data
        return Response(serializer)

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
