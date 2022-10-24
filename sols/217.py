class Solution:
    # Set (Acceted), O(n) time and space
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False

    # One Liner less than (Accepted), O(n) time and space
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

    # One Liner not equals (Top Voted), O(n) time and space
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
