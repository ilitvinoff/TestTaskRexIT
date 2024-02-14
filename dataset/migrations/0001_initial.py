# Generated by Django 4.2 on 2024-02-14 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dataset",
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
                ("category", models.CharField(blank=True, max_length=30, null=True)),
                ("firstname", models.CharField(blank=True, max_length=100, null=True)),
                ("lastname", models.CharField(blank=True, max_length=100, null=True)),
                ("email", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "gender",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, "Female"), (2, "MALE"), (3, "UNKNOWN")],
                        null=True,
                    ),
                ),
                ("birthDate", models.DateField(blank=True, default=None, null=True)),
            ],
        ),
    ]
