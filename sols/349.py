class Solution:
    # # Set Intersection (Accepted), O(n * m) time, O(n + m) space
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     s1, s2 = set(nums1), set(nums2)
    #     res = s1.intersection(s2)
    #     return list(res)

    # Set Intersection (Top Voted), O(n * m) time, O(n + m) space
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
