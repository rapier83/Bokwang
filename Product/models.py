from typing import List, Any, Union

from django.db import models
from django.db.models import IntegerField, BooleanField, ForeignKey, CharField


class ProductName:
    ProductNumber = [(1, 2744), (2, 2704), (3, 2912), (4, 2798), (5, 982), (6, 1150)]
    Prefix = "RFL-"
    Suffix: List[Union[str, Any]] = [("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E"),
                                     ("F", "F"), ("G", "G"), ("H", "H"), ("I", "I"), ("J", "J"),
                                     ("K", "K"), ("L", "L"), ]
    Unit = "Inches"


class Specs(models.Model):
    Size      = models.FloatField(null=True)
    Thickness = models.FloatField(null=True)
    Height    = models.FloatField(null=True)

    class Meta:
        abstract = True


class Fins(Specs):
    FinType: CharField = models.CharField(max_length=10, null=True)


class Rug(Specs):
    Rug: CharField = models.CharField(max_length=10, null=True)


class Manifold:
    # From Top, From Left, From Right, Radius
    Radius  = models.FloatField()
    # Position of Center of Holes
    Top     = models.FloatField()
    # Position of Each Holes
    Left    = models.FloatField()
    Right   = models.FloatField()


class Product(models.Model):
    Number   : IntegerField = models.IntegerField(choices=ProductName.ProductNumber)
    Prefix   : BooleanField = models.BooleanField(default=False)
    Suffix   : CharField = models.CharField(choices=ProductName.Suffix)
    NumberOfFins = models.IntegerField(null=True)




