from datetime import datetime
from collections import defaultdict
from .enums import CabState

class City:
    def __init__(self, city_id):
        self.city_id = city_id
        self.cabs = []
        self.request_log = defaultdict(int)  

    def add_cab(self, cab):
        self.cabs.append(cab)
        cab.update_location(self.city_id)
    
    def remove_cab(self, cab):
        if cab in self.cabs:
            self.cabs.remove(cab)

    def log_request(self, current_time=None):
        
        if current_time is None:
            current_time = datetime.now()
        
        self.request_log[current_time] += 1

    def peak_demand(self):
        
        if not self.request_log:
            return None
        
        peak_time = max(self.request_log, key=self.request_log.get)
        return peak_time, self.request_log[peak_time]
    
    def get_idle_cabs(self):
        """Return a list of cabs that are currently idle."""
        return [cab for cab in self.cabs if cab.state == CabState.IDLE]

    def __repr__(self):
        return f"City({self.city_id})"
