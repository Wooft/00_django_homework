from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=100)

class Tempchanges(models.Model):
    sensor = models.ForeignKey()
    temperature = models.FloatField()
    date = models.DateTimeField()
