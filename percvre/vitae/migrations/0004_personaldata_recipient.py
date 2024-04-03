# Generated by Django 5.0.3 on 2024-04-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vitae", "0003_alter_education_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="PersonalData",
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
                ("at_a_glance", models.TextField()),
                ("name", models.TextField()),
                ("place_of_birth", models.TextField()),
                ("date_of_birth", models.DateField()),
                ("telephone", models.TextField()),
                ("nationality", models.TextField()),
                ("address_zip", models.TextField()),
                ("address_city", models.TextField()),
                ("address_street", models.TextField()),
            ],
            options={
                "verbose_name": "Personal data",
                "verbose_name_plural": "Personal data",
            },
        ),
        migrations.CreateModel(
            name="Recipient",
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
                ("name", models.CharField(max_length=128)),
                ("token", models.CharField(max_length=64)),
            ],
            options={
                "verbose_name": "Recipient",
                "verbose_name_plural": "Recipients",
            },
        ),
    ]