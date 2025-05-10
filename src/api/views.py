from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Hotel, Reservation
from .serializers import HotelSerializer, ReservationSerializer


@api_view(["GET"])
def get_rooms(request):
    result = Hotel.objects.all().order_by("price")
    serializer = HotelSerializer(result, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_room(request):
    serializer = HotelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Комната отеля успешно создана"}, status=200)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def del_room(request, room_id: int):
    room = get_object_or_404(Hotel, pk=room_id)
    room.delete()
    return Response({"message": "Номер успешно удалён"}, status=204)


@api_view(["POST"])
def book_room(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid() and serializer.validate(data=request.data):
        reservation = serializer.save()
        booking_id = reservation.id
        return Response({"booking_id": booking_id})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_bookings(request, room_id: int):
    result = Reservation.objects.filter(hotel_room=room_id).order_by("date_start")
    serializer = ReservationSerializer(result, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def del_booking(request, booking_id: int):
    booking = get_object_or_404(Reservation, pk=booking_id)
    booking.delete()
    return Response({"message": "Бронь успешно удалена"}, status=204)
