# Generated by Django 2.2.10 on 2023-03-02 17:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("villes", "0003_auto_20230302_1354"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ville",
            name="code_postal",
        ),
    ]
