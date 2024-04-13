from models.cab import Cab

class CabService:
    def __init__(self):
        self.cabs = {}  

    def register_cab(self, cab):
        if cab in self.cabs:
            raise ValueError("Cab with this ID already exists.")
        self.cabs[cab.cab_id] = cab
        return cab

    def update_cab_state(self, cab_id, new_state, timestamp):
        if cab_id not in self.cabs:
            raise KeyError("No such cab found.")
        self.cabs[cab_id].update_state(new_state, timestamp)
