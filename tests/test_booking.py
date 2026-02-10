import allure
import pytest
import requests
import jsonschema
from tests.schemas.booking_schema import BOOKING_SCHEMA

@allure.feature('Test booking')
@allure.story('Test create booking')
def test_create_booking(api_client):
    payload = {
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2027-01-01",
            "checkout" : "2027-01-10"
        },
        "additionalneeds" : "Breakfast"
    }
    response_json = api_client.create_booking(payload)
    jsonschema.validate(response_json, BOOKING_SCHEMA)

    assert response_json["booking"]["firstname"] == payload["firstname"], "firstname не совпадает с ожидаемым"
    assert response_json["booking"]["lastname"] == payload["lastname"], "lastname не совпадает с ожидаемым"
    assert response_json["booking"]["totalprice"] == payload["totalprice"], "totalprice не совпадает с ожидаемым"
    assert response_json["booking"]["depositpaid"] == payload["depositpaid"], "depositpaid не совпадает с ожидаемым"
    assert response_json["booking"]["bookingdates"] == payload["bookingdates"], "bookingdates не совпадает с ожидаемым"
    assert response_json["booking"]["additionalneeds"] == payload["additionalneeds"], "additionalneeds не совпадает с ожидаемым"