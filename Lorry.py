from Vehicle import Vehicle


class Lorry(Vehicle):

    def __init__(self, reg_num, weight):
        super().__init__("Lorry", reg_num, weight)

    def calculateFee(self):
        if self.weight > 8000:
            return float(15.00)
        return float(10.00)

    def __repr__(self):
        return "Lorry=({}, {}, {})".format(self.vehicle_type, self.reg_num, self.weight)
