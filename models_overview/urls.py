from django.urls import path
from .views import PlaceList, RestaurantList

urlpatterns = [
    path('place/', PlaceList.as_view()),
    path('restaurant/', RestaurantList.as_view()),
]
