# Generated by Django 5.1.3 on 2024-11-21 21:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookstore", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="time_create",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]