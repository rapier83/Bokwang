from typing import List, Any, Union

from django.db import models
from django.db.models import EmailField, CharField, IntegerField, FloatField, BooleanField, UUIDField

# Create your models here.

class ProductName:
    ProductNumber = [(1, 2744), (2, 2704), (3, 2912), (4, 2798), (5, 982), (6, 1150)]
    Prefix = "RFL-"
    Suffix: List[Union[str, Any]] = [("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E"),
                                     ("F", "F"), ("G", "G"), ("H", "H"), ("I", "I"), ("J", "J"),
                                     ("K", "K"), ("L", "L"),]


class Product(models.Model):
    ProductID: UUIDField    = models.UUIDField(primary_key=True, editable=False)
    Number   : IntegerField = models.IntegerField(choices=ProductName.ProductNumber)
    Prefix   : BooleanField = models.BooleanField(null=False)
    Suffix   : IntegerField = models.IntegerField(choices=ProductName.Suffix)

    class Manifold:
        def __str__(self):
            """Specs of Manifold"""

        class WaterHole:

            # From Top, From Left, From Right, Radius
            FromTop    = models.FloatField()
            FromLeft   = models.FloatField()
            FromRight  = models.FloatField()
            HoleRadius = models.FloatField()

    class Fin:
        def __str__(self):
            """Specs of Fins"""

        Size      = models.FloatField(null=False)
        Thickness = models.FloatField(null=False)
        Height    = models.FloatField(null=False)

        def SyncSpec(selfs):
            self.Width = self.Size
            self.Depth = self.Thickness

    class Rug:
        def __str__(self):
            """Specs for Rug"""

    Unit = "Inches"
    NumberOfFins: IntegerField = models.IntegerField(32)




