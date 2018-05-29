import uuid

from django.db import models


# Create your models here.

class Farm(models.Model):
    id = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid1)
    farm_name = models.CharField(max_length=255, unique=True)
    farm_latitude = models.FloatField(default=0.0)
    farm_longitude = models.FloatField(default=0.0)
    owner = models.CharField(max_length=255)

    def __repr__(self):
        return self.farm_name




