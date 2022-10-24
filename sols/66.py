class Solution:
    # Carry from right to left (Accepted), O(n) time, O(1) space
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            n = digits[i] + 1
            if n == 10:
                digits[i] = 0
            else:
                digits[i] = n
                return digits
        digits.insert(0, 1)
        return digits

    # Convert to Int and Back (Top Voted), O(n) time and space
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(num+1)]
