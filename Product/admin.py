from django.contrib import admin
from Product import models

# Register your models here.
admin.site.register(models.Length)
admin.site.register(models.Angle)
admin.site.register(models.Position)
admin.site.register(models.Weight)

admin.site.register(models.FIN)
admin.site.register(models.RUG)
admin.site.register(models.MANIFOLD)

admin.site.register(models.FINSHIELD)
