from datetime import datetime
from .enums import CabState

class Cab:
    def __init__(self, cab_id, cab_state, city_id):
        self.cab_id = cab_id
        self.city_id = city_id
        self.state = cab_state
        self.history = []
        self.update_history(self.state, self.city_id)

        if self.state == CabState.IDLE:
            self.last_idle_time = datetime.now()
        else:
            self.last_idle_time = None

    def update_location(self, city_id):
        self.city_id = city_id

    def update_state(self, new_state, timestamp):
        if not isinstance(new_state, CabState):
            raise ValueError("new_state must be an instance of CabState Enum")
        self.state = new_state
        self.update_history(new_state, self.city_id, timestamp)

        if new_state == CabState.IDLE:
            self.last_idle_time = timestamp
        else:
            self.last_idle_time = None

    def update_history(self, state, city_id, timestamp=None):
        if not timestamp:
            timestamp = datetime.now()
        self.history.append({'state': state.name, 'city_id': city_id, 'timestamp': timestamp})

    def calculate_idle_time(self, start_time, end_time):
        total_idle_time = 0
        was_idle = self.state == CabState.IDLE
        last_time = self.last_idle_time

        for record in self.history:
            if record['state'] == CabState.IDLE.name and record['timestamp'] >= start_time:
                was_idle = True
                last_time = record['timestamp']
            elif record['state'] != CabState.IDLE.name and was_idle:
                if record['timestamp'] <= end_time:
                    total_idle_time += (record['timestamp'] - last_time).total_seconds()
                else:
                    total_idle_time += (end_time - last_time).total_seconds()
                was_idle = False

        if was_idle and last_time < end_time:
            total_idle_time += (end_time - last_time).total_seconds()

        return total_idle_time

    def __repr__(self):
        return f"Cab({self.cab_id}, {self.city_id}, {self.state.name})"
