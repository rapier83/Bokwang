from django.db import models
# from django.db.models import IntegerField, BooleanField,\
#                             CharField, FloatField, \
#                             DecimalField


class Properties:
    ProductNumber = [(2744, 2744), (2704, 2704), (2912, 2912), (2798, 2798), (982, 982), (1150, 1150)]
    Prefix = "RFL-"
    Suffix = [("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E"),
              ("F", "F"), ("G", "G"), ("H", "H"), ("I", "I"), ("J", "J"),
              ("K", "K"), ("L", "L"), ]
    Unit   = [("Inches", "Inches"), ("Degree", "Degree"), ("Metric", "Metric"), ("Kg", "kilogram"), ("lbs.", "Pounds")]

# Features

class Size(models.Model):
    Unit      = models.IntegerField(choices=Properties.Unit)
    Length    = models.FloatField(null=True, help_text="Size")
    Broad     = models.FloatField(null=True, help_text="Width")
    Thickness = models.FloatField(null=True, help_text="Depth")


class Weight(models.Model):
    Unit      = models.IntegerField(choices=Properties.Unit, default=4)
    Val       = models.FloatField(null=True)


class Position(models.Model):
    Unit      = models.IntegerField(choices=Properties.Unit)
    CENTERED  = models.BooleanField(null=True, default=True)
    FROMTOP   = models.FloatField(null=True)
    FROMLEFT  = models.FloatField(null=True)
    FROMRIGHT = models.FloatField(null=True)


class Angle(models.Model):
    Decimal   = models.DecimalField(null=True)
    Flt       = models.FloatField(null=True)

# Parts

class FIN(models.Model):
    Unit      = models.IntegerField(null=True)
    ORDER     = models.IntegerField(null=True)

    FINSize  = models.OneToOneField(Size, on_delete=models.CASCADE)
    Quantity = models.ManyToManyField('self')

    @property
    def FinList(self):
        return list(self.Quantity.all())


class RUG(models.Model):
    RUGPos  = models.OneToOneField(Position, on_delete=models.CASCADE)
    RUGSize = models.OneToOneField(Size, on_delete=models.CASCADE)


class MANIFOLD(models.Model):
    MANIFOLDSize = models.OneToOneField(Size, on_delete=models.CASCADE)

    HolePos   = models.OneToOneField(Position, on_delete=models.CASCADE)
    HoleRad   = models.FloatField()
    HoleWidth = models.FloatField()
    HoleThick = models.FloatField()


class FINSHIELD(models.Model):
    Number   = models.IntegerField(choices=Properties.ProductNumber)
    Prefix   = models.BooleanField(default=False)
    Suffix   = models.CharField(choices=Properties.Suffix)

    FinFeature = models.OneToOneField(FIN, on_delete=models.CASCADE)
    RugFeature = models.OneToOneField(RUG, on_delete=models.CASCADE)
    Manifold   = models.OneToOneField(Size, on_delete=models.CASCADE)

    Weight     = models.OneToOneField(Weight, on_delete=models.CASCADE)
