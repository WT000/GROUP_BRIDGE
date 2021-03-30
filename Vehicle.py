from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, vehicle_type, reg_num, weight):
        self.vehicle_type = vehicle_type
        self.reg_num = reg_num
        self.weight = weight

    @abstractmethod
    def calculateFee(self):
        pass

    def __repr__(self):
        return "Vehicle=({}, {}, {})".format(self.vehicle_type, self.reg_num, self.weight)