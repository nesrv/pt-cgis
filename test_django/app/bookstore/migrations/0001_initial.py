# Generated by Django 5.1.3 on 2024-11-21 19:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.TextField()),
                ("author", models.CharField(max_length=100)),
                ("price", models.IntegerField()),
                ("time_create", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
