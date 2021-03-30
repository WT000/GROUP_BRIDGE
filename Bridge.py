# Import the vehicle classes
from Motorbike import Motorbike
from Lorry import Lorry
from Car import Car


class Bridge:
    def __init__(self):
        self.vehicles = []

    def calc_total_weight(self):
        # Go through each vehicle in the list and add its weight onto the total
        total_weight = 0

        # Add the total weights
        for vehicle in self.vehicles:
            total_weight += vehicle.weight

        # If on or above 30k kg, return False (don't add), else return True (fine to add)
        return total_weight

    def add_vehicle(self, vehicle_to_add):
        if len(self.vehicles) <= 20:
            if self.calc_total_weight() + vehicle_to_add.weight <= 30000:
                self.vehicles.append(vehicle_to_add)
                return True
        return False

    def remove_car(self, reg_to_find):
        if len(self.vehicles) == 0:
            return False

        for vehicle in self.vehicles:
            if vehicle.reg_num == reg_to_find:
                self.vehicles.remove(vehicle)
                return True
        return False

    def __repr__(self):
        return "Bridge=(vehicles={})".format(self.vehicles)


if __name__ == '__main__':
    bridges = Bridge()
    motorbike1 = Motorbike("motorbike1", 5050, 1250)

    bridges.add_vehicle(motorbike1)
    print(bridges)
