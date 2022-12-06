from django.db import models


class PredResults(models.Model):

    from_source = models.CharField(max_length=100)
    to_destination = models.CharField(max_length=100)
    distance = models.FloatField()
    fuel_price = models.FloatField()
    fuel_consumption = models.FloatField()
    result = models.FloatField()

    def __float__(self):
        return self.result


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=700)

    def __str__(self):
        return self.message
