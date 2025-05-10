import pytest

from django.core.management import call_command
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.fixture(autouse=True)
def load_data(db):
    call_command("loaddata", "test_booking.json", "test_hotel_room.json")


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_get_rooms(api_client):
    url = reverse("get_rooms")
    response = api_client.get(url)
    assert response.status_code == 200
    prices = [item["price"] for item in response.data]
    assert prices == sorted(prices)


@pytest.mark.django_db
def test_create_room(api_client):
    url = reverse("create_room")
    data = {"hotel_room": 4, "price": 200, "description": "Vip номер."}
    response = api_client.post(url, data, format="json")
    assert response.status_code == 200
    assert response.data.get("message") == "Комната отеля успешно создана"


@pytest.mark.django_db
def test_delete_room(api_client):
    room_id = 1
    url = reverse("delete_room", args=[room_id])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert response.data.get("message") == "Номер успешно удалён"


@pytest.mark.django_db
def test_book_room(api_client):
    data = {"hotel_room": 1, "date_start": "2024-11-02", "date_end": "2024-12-03"}
    url = reverse("book_room")
    response = api_client.post(url, data, format="json")
    assert response.status_code == 200
    assert response.data.get("booking_id") == 4


@pytest.mark.django_db
def test_get_booking(api_client):
    room_id = 2
    url = reverse("get_bookings", args=[room_id])
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_del_booking(api_client):
    booking_id = 1
    url = reverse("delete_booking", args=[booking_id])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert response.data.get("message") == "Бронь успешно удалена"
