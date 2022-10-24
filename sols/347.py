from collections import Counter
from itertools import chain


class Solution:
    # Counter Most Common (Accepted), O(n log k) time, O(n) space
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        common = Counter(nums).most_common(k)
        res = []
        for key, _ in common:
            res.append(key)
        return res

    # Bucket Sort (Top Voted), O(n) time and space
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums).items()
        for num, freq in Count:
            bucket[freq].append(num)
        flat_list = list(chain(*bucket))
        return flat_list[::-1][:k]
