import unittest
from unittest.mock import MagicMock


class Cab:
    def __init__(self, cab_id):
        self.cab_id = cab_id
        self.state = None

    def update_state(self, new_state, timestamp):
        self.state = new_state

class City:
    def __init__(self, city_id):
        self.city_id = city_id
        self.cabs = []

    def add_cab(self, cab):
        self.cabs.append(cab)

class BookingService:
    def __init__(self, cab_service, city_service):
        self.cab_service = cab_service
        self.city_service = city_service

    def book_cab(self, city, request_time):
        if not city.cabs:
            return None
        return city.cabs[0]  
    
class CabService:
    def __init__(self):
        self.cabs = {}

    def register_cab(self, cab):
        if cab.cab_id in self.cabs:
            raise ValueError("Cab with this ID already exists.")
        self.cabs[cab.cab_id] = cab
        return cab

    def update_cab_state(self, cab_id, new_state, timestamp):
        if cab_id not in self.cabs:
            raise KeyError("No such cab found.")
        self.cabs[cab_id].update_state(new_state, timestamp)

class CityService:
    def __init__(self):
        self.cities = {}

    def onboard_city(self, city):
        if city.city_id in self.cities:
            raise ValueError("City with this ID already exists.")
        self.cities[city.city_id] = city
        return city

class TestCabService(unittest.TestCase):
    def setUp(self):
        self.cab_service = CabService()
        self.cab = Cab(1)
        self.timestamp = '2023-04-10 12:00:00'

    def test_register_cab_success(self):
        registered_cab = self.cab_service.register_cab(self.cab)
        self.assertEqual(registered_cab, self.cab)

    def test_register_cab_failure(self):
        self.cab_service.register_cab(self.cab)
        with self.assertRaises(ValueError):
            self.cab_service.register_cab(self.cab)

    def test_update_cab_state_success(self):
        self.cab_service.register_cab(self.cab)
        self.cab_service.update_cab_state(1, 'ON_TRIP', self.timestamp)
        self.assertEqual(self.cab.state, 'ON_TRIP')

    def test_update_cab_state_failure(self):
        with self.assertRaises(KeyError):
            self.cab_service.update_cab_state(99, 'ON_TRIP', self.timestamp)

class TestCityService(unittest.TestCase):
    def setUp(self):
        self.city_service = CityService()
        self.city = City(101)

    def test_onboard_city_success(self):
        onboarded_city = self.city_service.onboard_city(self.city)
        self.assertEqual(onboarded_city, self.city)

    def test_onboard_city_failure(self):
        self.city_service.onboard_city(self.city)
        with self.assertRaises(ValueError):
            self.city_service.onboard_city(self.city)

class TestBookingService(unittest.TestCase):
    def setUp(self):
        self.cab_service = MagicMock()
        self.city_service = MagicMock()
        self.booking_service = BookingService(self.cab_service, self.city_service)
        self.city = City(101)
        self.cab = Cab(1)
        self.city.add_cab(self.cab)

    def test_book_cab_success(self):
        booked_cab = self.booking_service.book_cab(self.city, '2023-04-10 12:00:00')
        self.assertEqual(booked_cab, self.cab)

    def test_book_cab_no_cabs(self):
        empty_city = City(102)
        result = self.booking_service.book_cab(empty_city, '2023-04-10 12:00:00')
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
