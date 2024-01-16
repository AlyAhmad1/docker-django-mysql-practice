from django.db import models
import uuid

# Create your models here.


class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Place(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.name} the place"


class Restaurant(BaseModel, models.Model):
    name = models.CharField(max_length=50)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    serves_hot_dogs = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.place.name} the restaurant"
