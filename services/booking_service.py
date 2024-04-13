from models.enums import CabState

class BookingService:
    def __init__(self, cab_service, city_service):
        self.cab_service = cab_service
        self.city_service = city_service

    def book_cab(self, city, request_time):
        
        city.log_request(request_time)
        idle_cabs = city.get_idle_cabs()
        if not idle_cabs:
            return None
        
        selected_cab = sorted(idle_cabs, key=lambda cab: cab.last_idle_time)[0]
        self.cab_service.update_cab_state(selected_cab.cab_id, CabState.ON_TRIP, request_time)
        return selected_cab
