class BMW:
    def fuel_type(self):
        return "Petrol"
    
    def max_speed(self):
        return 250

class Ferrari:
    def fuel_type(self):
        return "Petrol"
    
    def max_speed(self):
        return 320

def car_info(car):
    print(f"The car runs on {car.fuel_type()} and has a maximum speed of {car.max_speed()} km/h.")

bmw_car = BMW()
ferrari_car = Ferrari()

car_info(bmw_car)
car_info(ferrari_car)
