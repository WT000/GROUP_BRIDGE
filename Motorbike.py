from Vehicle import Vehicle


class Motorbike(Vehicle):

    def __init__(self, vehicle_type, reg_num, weight):
        pass

    def calculateFee(self):
        return 3.00

    def __repr__(self):
        return "Motorbike=({}, {}, {})".format(self.vehicle_type, self.reg_num, self.weight)