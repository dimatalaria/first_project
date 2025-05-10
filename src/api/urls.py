from django.urls import path
from . import views

urlpatterns = [
    path("create_room/", views.create_room, name="create_room"),
    path("get_rooms/", views.get_rooms, name="get_rooms"),
    path("del_room/<int:room_id>/", views.del_room, name="delete_room"),
    path("book_room/", views.book_room, name="book_room"),
    path("get_bookings/<int:room_id>/", views.get_bookings, name="get_bookings"),
    path("del_booking/<int:booking_id>/", views.del_booking, name="delete_booking"),
]
