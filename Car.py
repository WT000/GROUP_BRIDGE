from Vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, reg_num, weight):
        super().__init__("Car", reg_num, weight)

    def calculateFee(self):
        average_weight = 1590
        fee = float(5.00)

        if self.weight < average_weight:
            return fee

        # Calculate the additional weight
        additional_weight = (self.weight - average_weight)

        # Get how many times it's exceeded 100kg
        every_100 = additional_weight / 100

        # Return the fee + 0.10 for every 100kg
        return fee + (every_100 * 0.10)

    def __repr__(self):
        return "Car=({}, {}, {})".format(self.vehicle_type, self.reg_num, self.weight)
