class Solution:
    # Zeros and non-zeros swap (Accepted), O(n) time, O(1) space
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return nums

        z, nz = 0, 1
        while nz < n:
            if nums[nz] == 0 or nz <= z:
                nz += 1
            elif nums[z] != 0:
                z += 1
            else:
                nums[nz], nums[z] = nums[z], nums[nz]
                z, nz = z+1, nz+1

    # Pythonic Optimal Swap (Top Voted), O(n) time, O(1) space
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
