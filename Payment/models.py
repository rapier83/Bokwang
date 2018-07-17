from django.db import models
from django.db.models import EmailField, CharField, DateField, BooleanField
from django.core.files.storage import FileSystemStorage
import django.utils

RequestStorage = FileSystemStorage()
StorageLocation = '/Payment/Storage/Orders'

# Scenario
# 1. check email
# 2. check header?


# Mark : - 1. Orders

class Order(models.Model):
    SenderEmail   : EmailField = models.EmailField()
    OrderedCompany: CharField = models.CharField(max_length=50)
    ThePaper      : CharField = models.FileField(upload_to='Order Request', storage=RequestStorage,
                                                blank=False, null=False)
    DeliveredDate : DateField    = models.DateField(null=False)
    Confirmed_date: DateField    = models.DateField(null=False)
    LastUpload    : DateField    = models.DateField(default=django.utils.timezone.now, blank=True, null=False)
    isStored      : BooleanField = models.BooleanField(default=False, null=False)

    def SetLocation(self):
        self.FollowLocation = self.DeliveredDate.clone()

    def __str__(self):
        return self.title

    def __init__(self):
        pass


# Mark : - 2. Products

