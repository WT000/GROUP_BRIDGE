from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, reg_num, weight):
        super().__init__("Car", reg_num, weight)

    def calculateFee(self):
        average_weight = 1590
        fee = float(5.00)

        if self.weight < average_weight:
            return fee

        # if the car weight is greater than 1590, add 10p per 100kg excess
        while average_weight < self.weight:
            fee += 0.1
            average_weight += 100

        fee = "%.1f" % fee

        return float(fee)
