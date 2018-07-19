from datetime import datetime

from django.db import models
from django.db.models import EmailField, CharField, DateField, BooleanField
from django.core.files.storage import FileSystemStorage
import django.utils

RequestStorage = FileSystemStorage()
StorageLocation = '/Payment/Storage/Orders'


# Mark : - 1. Orders

class Order(models.Model):

    def __str__(self):
        """Orders are two kinds. First is Purchase order, it's from Our client-Plant Kimcheon, OC Korea- or oversee.
         So, thar need to be archived, and don't make miss. Specially, Like missing order, late check make a catastrophic
         accident"""

    def __init__(self):
        self.SaveLocation = None

    class Paper:
        # Model Entries(Product).
        # Recommend write the Optional.
        # Mark: - Scenario
        ## 1. input PDF file receive from the orderer
        ## 2. check it's parserable.
        ## 3. If it is, input Automatically
        ## 4. If it is NOT, it should input Manually, (Almost entries are Not Null)
        ## 5. Alert User input manually
        ## 6. Check another user, notice by e-mail or MMS

        SenderEmail: EmailField = models.EmailField()
        OrderedCompany: CharField = models.CharField(max_length=50)
        ThePaper: CharField = models.FileField(upload_to='Order Request', storage=RequestStorage,
                                               blank=False, null=False)
        DeliveredDate: DateField = models.DateField(null=False)
        Confirmed_date: DateField = models.DateField(null=False)
        LastUpload: DateField = models.DateField(default=django.utils.timezone.now, blank=True, null=False)
        isStored: BooleanField = models.BooleanField(default=False, null=False)

        def SetLocation(self):
            self.SaveLocation = StorageLocation + '/' + self.DeliveredDate.clone()

        def DateCheck(self, t):
            def isFirst(self, b):
                self.ReadFirst = (t, b)
                return self.ReceivedDate

            return isFirst(True)

