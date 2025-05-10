from rest_framework import serializers
from .models import Hotel, Reservation


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ["hotel_room", "price", "description"]


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["hotel_room", "date_start", "date_end"]

    def validate(self, data):
        hotel_room = data["hotel_room"]
        date_start = data["date_start"]
        date_end = data["date_end"]
        if date_start >= date_end:
            raise serializers.ValidationError(
                "Дата окончания не может быть раньше даты начала или одинаковыми!"
            )
        existing_reservation = Reservation.objects.filter(
            hotel_room=hotel_room, date_start__lte=date_end, date_end__gte=date_start
        )

        if existing_reservation.exists():
            raise serializers.ValidationError("Номер уже забронирован на данное время")
        return data
