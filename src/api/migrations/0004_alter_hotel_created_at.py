# Generated by Django 5.2 on 2025-04-20 06:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_hotel_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hotel",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
