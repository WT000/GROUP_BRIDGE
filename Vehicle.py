from _abc import

class Vehicle:

    def __init__(self, reg_num, weight):
        self.reg_num = reg_num
        self.weight = weight

    def calculateFee(self):
        pass
