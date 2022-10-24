class Solution:
    # Brute Force (Accepted), O(n^2) time, O(n) space
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for n in nums1:
            j = nums2.index(n)
            v = -1
            for n2 in nums2[j+1:]:
                if n2 > n:
                    v = n2
                    break
            res.append(v)
        return res

    # Stack and Dict (Top Voted), O(n) time and space
    def nextGreaterElement(self, findNums: List[int], nums: List[int]) -> List[int]:
        st, d = [], {}
        for n in nums:
            while st and st[-1] < n:
                d[st.pop()] = n
            st.append(n)

        return [d.get(x, -1) for x in findNums]
