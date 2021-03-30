from Vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, reg_num, weight, vehicle_type):
        super().__init__(vehicle_type, reg_num, weight)
        self.reg_num = reg_num
        self.weight = weight

    def calculateFee(self):
        average = 1590
        fee = float(5.00)
        if self.weight < average:
            return fee
        elif self.weight > average:
            while self.weight > average + 100:
                fee + float(0.10)
                if average == self.weight:
                    return fee
        else:
            return fee


