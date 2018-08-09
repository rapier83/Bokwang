
from django.db import models
from django.db.models import EmailField, CharField, DateField, BooleanField, ForeignKey
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

RequestStorage = FileSystemStorage()
StorageLocation = 'Payment/Storage/Orders'


# Mark : - 1. Orders

class Order(models.Model):
    # Model Entries(Product).
    # Recommend write the Optional.
    # Mark: - Scenario
    ## 1. input PDF file receive from the orderer
    ## 2. check if it possible to parse
    ## 3. If it is, input Automatically
    ## 4. If it is NOT, it should input Manually, (Almost entries are Not Null)
    ## 5. Alert User input manually
    ## 6. Check another user, notice by e-mail or MMS

    SaveLocation = None
    SenderEmail   : EmailField   = models.EmailField()
    OrderedCompany: CharField    = models.CharField(max_length=50)
    ThePaper      : CharField    = models.FileField(upload_to=StorageLocation, storage=RequestStorage)
    DeliveredDate : DateField    = models.DateField(null=True, default=None)
    LastQueryTime : DateField    = models.DateField(null=True, default=None)
    ConfirmedDate : DateField    = models.DateField(null=True, default=None)
    UploadDate    : DateField    = models.DateField(null=True, default=None)
    DueDate       : DateField    = models.DateField(null=True)
    isStored      : BooleanField = models.BooleanField(default=False, null=False)
    Goods         : ForeignKey   = models.ForeignKey('Product.Product', on_delete=models.CASCADE,)

    def publish(self):
        self.LastQueryTime = timezone.now()
        self.save()

    def __str__(self):
        """Orders are two kinds. First is Purchase order, it's from Our client-Plant Kimcheon, OC Korea- or oversee.
        So, thar need to be archived, and don't make miss. Specially, Like missing order, late check make a catastrophic
        accident"""

        return f'{self.Goods} {self.DeliveredDate} by f{self.DueDate}'


# Mark: - 2. Manager

class OrderManage(models.Manager):

    @staticmethod
    def isDateExist() -> bool:
        if Order.DeliveredDate:
            return True
        else:
            return False
