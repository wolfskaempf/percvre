# Generated by Django 5.0.3 on 2024-04-03 13:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vitae", "0002_reference"),
    ]

    operations = [
        migrations.AlterField(
            model_name="education",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
