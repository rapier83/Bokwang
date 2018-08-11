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
    LengthType   = [("Inches", "\""), ("Metric(mm)", "mm"), ]
    WeightType   = [("Pounds", "lbs."), ("Kilogram", "kg"), ]
    AngleType    = [("Degree", "°"), ("Radian", "(rad)"), ]


# Features
class REC(models.Model):
    # REC for Manifold,
    REC_UNIT = models.CharField(choices=Properties.LengthType, max_length=20)
    LENGTH   = models.FloatField(blank=True, help_text="REC")
    WIDE     = models.FloatField(blank=True, help_text="Width")
    THICK    = models.FloatField(blank=True, help_text="Depth")

    def __str__(self):
        return f'{self.LENTH: .3f}{self.REC_UNIT} X {self.WIDE: .3f}{self.REC_UNIT} X {self.THICK: .3f}{self.REC_UNIT}'


class Angle(models.Model):
    ANGLE_UNIT = models.CharField(choices=Properties.AngleType, max_length=10)
    ANGLE      = models.FloatField(blank=True, help_text="Degree")

    def __str__(self):
        return f'{self.Angle: .3f}{self.ANGLE_UNIT}'


class Weight(models.Model):
    WEIGHT_UNIT = models.CharField(choices=Properties.WeightType, max_length=10)
    WEIGHT      = models.FloatField(blank=True)

    def __str__(self):
        return f'{self.Weight: .3f}{self.WEIGHT_UNIT}'


class Position(models.Model):
    POS_UNIT = models.CharField(choices=Properties.LengthType, max_length=10)
    CENTERED = models.BooleanField(default=True)
    TOP      = models.FloatField(blank=True)
    LEFT     = models.FloatField(blank=True)
    RIGHT    = models.FloatField(blank=True)
    BOTTOM   = models.FloatField(blank=True)

    def __str__(self):
        return f'Left:  {self.FROMLEFT: .3f}{self.POS_UNIT} \n \
                 Right: {self.FROMRIGHT: .3f}{self.POS_UNIT} \n '


# Parts
# FIN can be products sometimes. (export to china)
class FIN(REC, Angle, models.Model):
    ORDER = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)],
                                                blank=True)
    def __str__(self):
        return f'{self.ORDER}: {self.LENGTH} {self.WIDE} {self.THICK} ({self.REC_UNIT}) {self.ANGLE}({self.ANGLE_UNIT})'

    class Meta:
        ordering = ('ORDER', )


class RUG(Position, REC, models.Model):

    def __str__(self):
        return f'{self.TOP} {self.LEFT} {self.RIGHT} | REC: {self.LENGTH} {self.WIDE} {self.THICK} {self.REC_UNIT}'


class MANIFOLD(REC, models.Model):
    RUG_INFO     = models.ForeignKey(RUG, on_delete=models.CASCADE)
    HOLE_POS     = models.ManyToManyField(Position)
    HOLE_R       = models.FloatField(blank=True)
    FLUTES_NUM   = models.IntegerField(blank=True)
    FLUTES_DEPTH = models.FloatField(blank=True)
    FLUTES_ANGLE = models.ManyToManyField(Angle)

    def __str__(self):
        return f'{self.LENGTH} {self.WIDE} {self.THICK} {self.REC_UNIT} {self.RUG_INFO}        {self.HOLE_R}'


# Product
class FINSHIELD(models.Model):
    # A finshield name
    Number   = models.IntegerField(choices=Properties.ProductNumber,)
    Prefix   = models.BooleanField(default=False, max_length=5)
    Suffix   = models.CharField(choices=Properties.Suffix, max_length=1)

    # the finshield spec
    Fins     = models.ManyToManyField(FIN)
    Rug      = models.ManyToManyField(RUG, blank=True)
    Manifold = models.ManyToManyField(MANIFOLD, blank=True)
    Weight   = models.ManyToManyField(Weight, blank=True)

    @property
    def FinList(self):
        return list(self.Fins.all())

    def __str__(self):
        return f'{self.Prefix} {self.Number} {self.Suffix}'

