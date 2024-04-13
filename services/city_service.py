from models.city import City

class CityService:
    def __init__(self):
        self.cities = {} 

    def onboard_city(self, city):
        if city.city_id in self.cities:
            raise ValueError("City with this ID already exists.")
        
        self.cities[city.city_id] = city
        return city
    
    def get_city(self, city):
        if city.city_id not in self.cities:
            raise KeyError("No such city found.")
        return self.cities[city.city_id]

    def get_idle_cabs_in_city(self, city):
        if city.city_id not in self.cities:
            raise KeyError("No such city found.")
        city.get_idle_cabs()
        
    
    def change_cab_city(self, cab, new_city):
        if new_city.city_id not in self.cities:
            raise KeyError("No such city found.")
        
        old_city = self.get_city(cab.city_id)
        
        old_city.remove_cab(cab)
        new_city.add_cab(cab)