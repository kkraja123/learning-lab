# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/description/

# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


class Solution:

    def fib(self, n: int) -> int:

        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


if __name__ == "__main__":
    solution = Solution()
    print(solution.fib(4)) # O(2^n) O(n)
