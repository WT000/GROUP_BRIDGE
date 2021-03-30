# Import the vehicle classes
from Motorbike import Motorbike
from Lorry import Lorry

class Bridge():
    def __init__(self):
        self.vehicles = []

    def calc_total_weight(self):
        # Go through each vehicle in the list and add its weight onto the total
        total_weight = 0

        # Add the total weights
        for vehicle in self.vehicles:
            total_weight += vehicle.weight

        # If on or above 30k kg, return False (don't add), else return True (fine to add)
        if total_weight >= 30000:
            return False
        else:
            return total_weight, True

    def add_vehicle(self, vehicle_to_add):
        if len(self.vehicles) <= 20 and vehicle_to_add.weight:
            self.vehicles.append(vehicle_to_add)
            return True
        return False

    def remove_car(self, reg_to_find):
        for vehicle in self.vehicles:
            if vehicle.reg_num == reg_to_find:
                self.vehicles.remove(vehicle)
                return True
        return False
