class Solution:
    # Assign on discontiguous (Accepted), O(n) time, O(1) space
    def checkZeroOnes(self, s: str) -> bool:
        l0 = l1 = cnt = 0
        prev = None

        for cur in s:
            if cur == prev:
                cnt += 1
            else:
                if prev == '1':
                    l1 = max(cnt, l1)
                else:
                    l0 = max(cnt, l0)
                cnt = 1
            prev = cur

        if prev == '1':
            l1 = max(cnt, l1)
        else:
            l0 = max(cnt, l0)

        return l1 > l0

    # Simple Solution (Top Voted), O(n) time, O(1) space
    def checkZeroOnes(self, s: str) -> bool:
        best_one, best_zero, current_one, current_zero = 0, 0, 0, 0

        for i in s:
            if i == "1":
                current_zero = 0
                current_one += 1
            else:
                current_zero += 1
                current_one = 0

            best_one = max(best_one, current_one)
            best_zero = max(best_zero, current_zero)

        return best_one > best_zero

    # Lists + Prev (Sample), O(n) time, O(1) space
    def checkZeroOnes(self, s: str) -> bool:
        longest = [0, 0]
        current = [0, 0]
        last = 0
        for char in s:
            num = int(char)
            if num != last:
                current[(num + 1) % 2] = 0
            current[num] += 1
            longest[num] = max(longest[num], current[num])
            last = num
        return longest[1] > longest[0]
