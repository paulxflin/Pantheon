class Solution:
    # # Binary Search (Accepted), O(n log n) time, O(1) space
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     def search(num, low, high):
    #         while low < high:
    #             mid = (low + high) // 2
    #             if numbers[mid] == num:
    #                 return mid
    #             elif numbers[mid] > num:
    #                 high = mid
    #             else:
    #                 low = mid+1
    #         return -1

    #     l = len(numbers)
    #     for i in range(l):
    #         n = search(target-numbers[i], i+1, l)
    #         if n != -1:
    #             res = [i+1, n+1]
    #             return res
    #     return []

    # # Hashmap (Accepted), O(n) time and space
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     d = {}
    #     for i in range(len(numbers)):
    #         n = numbers[i]
    #         if target-n in d:
    #             return [d[target-n], i+1]
    #         d[n] = i+1
    #     return []

    # Two pointer (Top Voted), O(n) time, O(1) space
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1
