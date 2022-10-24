class Solution:
    # # Reverse sort by unit per box + Greedy (Accepted), O(n log n) time, O(n) space, n is len(boxTypes)
    # def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
    #     def unit_per_box(box):
    #         return box[1]
    #     boxTypes.sort(reverse=True, key=unit_per_box)
    #     res = 0
    #     for box in boxTypes:
    #         if box[0] < truckSize:
    #             res += box[0] * box[1]
    #             truckSize -= box[0]
    #         else:
    #             return res + truckSize * box[1]
    #     return res

    # Reverse sort by units + Greedy (Top Voted), O(n log n) time, O(n) space
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        for box, units in boxTypes:
            if truckSize > box:
                truckSize -= box
                ans += box * units
            else:
                ans += truckSize * units
                return ans
        return ans
