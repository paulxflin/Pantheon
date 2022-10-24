class Solution:
    # # Greedy Simulation (Accepted), O(n) time, O(1) space
    # def lemonadeChange(self, bills: List[int]) -> bool:
    #     five = ten = 0
    #     for bill in bills:
    #         if bill == 5:
    #             five += 1
    #         elif bill == 10:
    #             if five > 0:
    #                 five -= 1
    #                 ten += 1
    #             else:
    #                 return False
    #         elif bill == 20:
    #             if ten > 0 and five > 0:
    #                 ten -= 1
    #                 five -= 1
    #             elif five >= 3:
    #                 five -= 3
    #             else:
    #                 return False
    #     return True

    # Greedy Simulation (Top Voted), O(n) time, O(1) space
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                five, ten = five - 1, ten + 1
            elif ten > 0:
                five, ten = five - 1, ten - 1
            else:
                five -= 3
            if five < 0:
                return False
        return True
