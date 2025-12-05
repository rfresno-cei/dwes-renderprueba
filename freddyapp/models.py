from django.db import models

# Create your models here.
class Party(models.Model):
    name = models.CharField()
    attendants = models.IntegerField()

class Animatronic(models.Model):
    name = models.CharField(max_length=50)
    types = [
        ('BE', 'Bear'),
        ('CH', 'Chicken'),
        ('BU', 'Bunny'),
        ('FO', 'Fox')
    ]
    animal = models.CharField(max_length=2, choices=types)
    build_date = models.DateField()
    decommissioned = models.BooleanField()
    parties = models.ManyToManyField(Party, blank=True)