# Generated by Django 5.2 on 2025-04-21 12:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_alter_reservation_hotel_room"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hotel",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
    ]
