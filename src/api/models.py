from django.db import models


class Hotel(models.Model):
    hotel_room = models.IntegerField(unique=True)
    price = models.IntegerField()
    description = models.TextField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.hotel_room)


class Reservation(models.Model):
    hotel_room = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, to_field="hotel_room"
    )
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return str(self.hotel_room)
