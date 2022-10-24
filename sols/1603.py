class ParkingSystem:

    # # Instance Variables (Accepted), O(1) time, O(1) space wrt addCar
    # def __init__(self, big: int, medium: int, small: int):
    #     self.big = big
    #     self.medium = medium
    #     self.small = small

    # def addCar(self, carType: int) -> bool:
    #     if carType == 1:
    #         if self.big > 0:
    #             self.big -= 1
    #             return True
    #     elif carType == 2:
    #         if self.medium > 0:
    #             self.medium -= 1
    #             return True
    #     else:
    #         if self.small > 0:
    #             self.small -= 1
    #             return True
    #     return False

    # # Hashmap (Accepted), O(1) time and space wrt addCar
    # def __init__(self, big: int, medium: int, small: int):
    #     self.spaces = {}
    #     self.spaces[1] = big
    #     self.spaces[2] = medium
    #     self.spaces[3] = small

    # def addCar(self, carType: int) -> bool:
    #     if self.spaces[carType] > 0:
    #         self.spaces[carType] -= 1
    #         return True
    #     return False

    # Array (Top Voted), O(1) time, O(1) space wrt addCar
    def __init__(self, big, medium, small):
        self.A = [big, medium, small]

    def addCar(self, carType):
        self.A[carType - 1] -= 1
        return self.A[carType - 1] >= 0


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
