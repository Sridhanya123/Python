class vehicle:
    def __init__(self,vehicle_id,base_rate):
         self._vehicle_id=vehicle_id
         self._base_rate=base_rate
    def display_details(self):
         return "Vehicle_ID {self.vehicle_id},Base_Rate {self.base_rate}"
    def rental_charge(self):
         return 0.0
class car(vehicle):
     def __init__(self, vehicle_id, base_rate,num_seats):
          super().__init__(vehicle_id, base_rate)
          self.num_seats=num_seats
     def rental_charge(self):
          return self._base_rate*self.num_seats
class bike(vehicle):
     def __init__(self, vehicle_id, base_rate,bike_type):
          super().__init__(vehicle_id, base_rate)
          self.bike_type=bike_type
          
         
    
