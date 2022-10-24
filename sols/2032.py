class Solution:
    # Sets (Accepted), O(n) time and space, n = max(len(nums1), len(nums2), len(nums3))
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        return list((s1 & s2) | (s2 & s3) | (s3 & s1))

    # One Liner (Top Voted), O(n) time and space
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return set(nums1) & set(nums2) | set(nums2) & set(nums3) | set(nums1) & set(nums3)
