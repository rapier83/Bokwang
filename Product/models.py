from django.db import models
from django.core.validators import MinValueValidator
# from django.db.models import IntegerField, BooleanField,\
#                             CharField, FloatField, \
#                             DecimalField


class Properties:
    ProductNumber = [(2744, 2744), (2704, 2704), (2912, 2912), (2798, 2798), (982, 982), (1150, 1150)]
    Prefix = "RFL-"
    Suffix = [("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E"),
              ("F", "F"), ("G", "G"), ("H", "H"), ("I", "I"), ("J", "J"),
              ("K", "K"), ("L", "L"), ]
    LengthType   = [("Inches", "Inches"), ("Metric", "Metric"), ]
    WeightType   = [("lbs.", "Pounds"), ("Kg", "kilogram"), ]
    AngleType    = [("Degree", "Degree"), ("Radian", "Radian"), ]


# Features
class Length(models.Model):
    # Size for Manifold,
    CUBE_UNIT    = models.CharField(choices=Properties.LengthType, max_length=20)
    Length       = models.FloatField(null=True, blank=True, help_text="Size")
    Broad        = models.FloatField(null=True, blank=True, help_text="Width")
    Thickness    = models.FloatField(null=True, blank=True, help_text="Depth")


class Angle(models.Model):
    ANGLE_UNIT   = models.CharField(choices=Properties.AngleType, max_length=10)
    Angle        = models.FloatField(null=True, blank=True, help_text="Degree")


class Weight(models.Model):
    WEIGHT_UNIT  = models.CharField(choices=Properties.WeightType, max_length=10)
    Weight       = models.FloatField(null=True, blank=True)


class Position(models.Model):
    POS_UNIT     = models.CharField(choices=Properties.LengthType, max_length=10)
    CENTERED     = models.BooleanField(default=True)
    FROMTOP      = models.FloatField(null=True, blank=True)
    FROMLEFT     = models.FloatField(null=True, blank=True)
    FROMRIGHT    = models.FloatField(null=True, blank=True)


# Parts
# FIN can be products sometimes. (export to china)
class FIN(models.Model):
    FINOrder     = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)],
                                                    blank=True)
    FINSize      = models.OneToOneField(Length, on_delete=models.CASCADE)
    FINAngle     = models.OneToOneField(Angle, on_delete=models.CASCADE, blank=True)

    class Meta:
        ordering = ('FINOrder', )


class RUG(models.Model):
    RUGPos  = models.OneToOneField(Position, on_delete=models.CASCADE)
    RUGSize = models.OneToOneField(Length, on_delete=models.CASCADE)


class MANIFOLD(models.Model):
    DIMENSION = models.OneToOneField(Length, on_delete=models.CASCADE)
    HolePos   = models.OneToOneField(Position, on_delete=models.CASCADE)
    HoleRad   = models.FloatField()
    HoleWidth = models.FloatField()
    HoleThick = models.FloatField()


# Product
class FINSHIELD(models.Model):
    # A finshield name
    Number   = models.IntegerField(choices=Properties.ProductNumber,)
    Prefix   = models.BooleanField(default=False, max_length=5)
    Suffix   = models.CharField(choices=Properties.Suffix, max_length=1)

    # the finshield spec
    Fins     = models.ManyToManyField(FIN)
    Rug      = models.OneToOneField(RUG, on_delete=models.CASCADE)
    Manifold = models.OneToOneField(MANIFOLD, on_delete=models.CASCADE)
    Weight   = models.OneToOneField(Weight, on_delete=models.CASCADE)

    @property
    def FinList(self):
        return list(self.Fins.all())

    def __str__(self):
        return f'{self.Prefix} {self.Number} {self.Suffix}'

