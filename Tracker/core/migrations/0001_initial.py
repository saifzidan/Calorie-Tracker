# Generated by Django 4.2.7 on 2023-11-15 22:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Calorie",
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
                ("food", models.CharField(max_length=1000, null=True)),
                ("calories", models.PositiveIntegerField(null=True)),
                ("time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
