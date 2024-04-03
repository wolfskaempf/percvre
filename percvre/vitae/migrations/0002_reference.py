# Generated by Django 5.0.3 on 2024-04-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vitae", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reference",
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
                ("link", models.URLField()),
            ],
        ),
    ]
