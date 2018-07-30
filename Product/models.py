from typing import List, Any, Union

from django.db import models
from django.db.models import IntegerField, BooleanField, UUIDField


# Create your models here.
class ProductName:
    ProductNumber = [(1, 2744), (2, 2704), (3, 2912), (4, 2798), (5, 982), (6, 1150)]
    Prefix = "RFL-"
    Suffix: List[Union[str, Any]] = [("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E"),
                                     ("F", "F"), ("G", "G"), ("H", "H"), ("I", "I"), ("J", "J"),
                                     ("K", "K"), ("L", "L"),]


class Product(models.Model):
    Number   : IntegerField = models.IntegerField(choices=ProductName.ProductNumber)
    Prefix   : BooleanField = models.BooleanField(default=False)
    Suffix   : IntegerField = models.IntegerField(choices=ProductName.Suffix)
    ProductID: UUIDField    = models.UUIDField(max_length=20)

    class Manifold:
        def __str__(self):
            """Specs of Manifold"""

        class WaterHole:
            # From Top, From Left, From Right, Radius
            FromTop     = models.FloatField()
            LeftCenter  = models.FloatField()
            RightCenter = models.FloatField()
            HoleRadius  = models.FloatField()

    class Fin:
        def __str__(self):
            """Specs of Fins"""

        Size      = models.FloatField(null=False)
        Thickness = models.FloatField(null=False)
        Height    = models.FloatField(null=False)

    class Rug:
        def __str__(self):
            """Specs for Rug"""

    Unit = "Inches"
    NumberOfFins: IntegerField = models.IntegerField(32)


def SyncSpec(self):
    self.Width = self.Size
    self.Depth = self.Thickness



