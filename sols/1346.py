from collections import defaultdict, Counter


class Solution:
    # # Dict with List (Accepted), O(n) time and space
    # def checkIfExist(self, arr: List[int]) -> bool:
    #     nums = defaultdict(list)

    #     for i in range(len(arr)):
    #         nums[arr[i]] += [i]

    #     for n in arr:
    #         if n/2 in nums and not (n == 0 and len(nums[n]) == 1):
    #             return True

    # Counter (Accepted), O(n) time and space
    def checkIfExist(self, arr: List[int]) -> bool:
        s = Counter(arr)
        if s[0] > 1:
            return True

        for num in arr:
            if s[2*num] and num != 0:
                return True
        return False
