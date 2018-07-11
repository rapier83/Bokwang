from django.db import models
from django.db.models import DateTimeField, FileField
from django.utils import timezone
from django.core.files.storage import FileSystemStorage


class Order(models.Model):
    ReceiverEmail: CharField      = models.CharField(max_length = 200)
    OrderCompany : CharField      = models.CharField(max_length = 200)
    ThePaper     : CharField      = models.FileField(
        upload_to='Order Request',
        storage=OrderRequestStorage,
        blank=False, null=False, )
    DeliverdDate  : DateTimeField = models.DateTimeField(default=timezone.now)
    Confirmed_date: DateTimeField = models.DateTimeField(blank=True, null=True)

    def Confirm(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# Mark: - Set Order PDF file storage
OrderRequestStorage = FileSystemStorage()


class Peer(models.Model):
    PDFFileName          = models.CharField(max_length=20, unique=True)
    StoreFile: FileField = models.FileField(
        upload_to='Payment/OrderRequestStorage',
        storage=OrderRequestStorage,
        blank=True, null=True
    )