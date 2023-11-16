from django.db import models
class Calorie(models.Model):
    food = models.CharField(max_length=1000 , null=True)
    calories = models.FloatField(null=True)
    time = models.DateTimeField(auto_now_add=True)