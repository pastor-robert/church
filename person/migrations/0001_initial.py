# Generated by Django 4.2.7 on 2023-12-12 03:31

import address.models
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("address", "0003_auto_20200830_1851"),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("email_confirmed", models.BooleanField(default=False)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, region="US"
                    ),
                ),
                ("phone_number_confirmed", models.BooleanField(default=False)),
                (
                    "portrait",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                (
                    "address",
                    address.models.AddressField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="address.address",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
