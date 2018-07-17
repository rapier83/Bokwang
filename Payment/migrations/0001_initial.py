# Generated by Django 2.0.7 on 2018-07-16 10:55

import django.core.files.storage
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReceiverEmail', models.CharField(max_length=200)),
                ('OrderCompany', models.CharField(max_length=200)),
                ('ThePaper', models.FileField(storage=django.core.files.storage.FileSystemStorage(), upload_to='Order Request')),
                ('DeliveredDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('Confirmed_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Papers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PDFFileName', models.CharField(max_length=20, unique=True)),
                ('StoreFile', models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(), upload_to='Payment/OrderRequestStorage')),
            ],
        ),
    ]
