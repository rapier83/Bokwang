from django.db import models
from django.db.models import EmailField, CharField, IntegerField, FloatField, BooleanField, UUIDField

# Create your models here.

class ProductName:
    ProductNumber = [2744, 2704, 2912, 2798, 982, 1150]
    Prefix = "RFL-"
    Surfix = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]


class Product(models.Model):
    ProductID: UUIDField    = models.UUIDField(primary_key=True, editable=False)
    Name     : IntegerField = models.CharField(max_length=5, choices=ProductName.ProductNumber)
    Prefix   : BooleanField = models.BooleanField(null=True)
    Surfix   : CharField    = models.CharField(max_length=2, choices=ProductName.Surfix)

    class Specs:
        Unit = "Inches"
        NumberOfFins = models.IntegerField(32)

        class Manifold:
            class WaterHole:
                # From Top, From Left, From Right, Radius
                FromTop    = models.FloatField()
                FromLeft   = models.FloatField()
                FromRight  = models.FloatField()
                HoleRadius = models.FloatField()
            def __str__(self):
                """Specs of Manifold"""

        class Fin:

            def __str__(self):
                """Specs of Fins"""

        class Rug:

            def __str__(self):
                """Specs for Rug"""




