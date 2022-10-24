from collections import Counter


class Solution:
    # Counter (Accepted), O(n+m) time and space
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1, c2 = Counter(nums1), Counter(nums2)
        c = c1 if len(nums1) < len(nums2) else c2
        res = []
        for n in c:
            for _ in range(min(c1[n], c2[n])):
                res.append(n)
        return res

    # Counter (Top Voted), O(n+m) time and space
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        res = []

        for num in nums2:
            if counts[num] > 0:
                res += num,
                counts[num] -= 1

        return res
