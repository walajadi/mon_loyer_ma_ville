# Generated by Django 2.2.10 on 2023-03-02 12:32

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ville",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted", models.BooleanField(default=False)),
                (
                    "code_insee",
                    models.CharField(
                        help_text="Code INSEE de la ville.", max_length=128
                    ),
                ),
                (
                    "code_postal",
                    models.CharField(
                        help_text="Code postal de la ville.", max_length=128
                    ),
                ),
                ("nom", models.CharField(help_text="Nom de la ville.", max_length=256)),
                ("loyer_moyen", models.FloatField(help_text="Loyer moyen.", null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
