class Solution:
    # if-elif-else (Accepted), O(n) time and space
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for n in range(1, n+1):
            if n % 15 == 0:
                ans.append('FizzBuzz')
            elif n % 3 == 0:
                ans.append('Fizz')
            elif n % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(n))
        return ans

    # List comprehension One-liner (Top Voted), O(n) time and space
    def fizzBuzz(self, n: int) -> List[str]:
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
