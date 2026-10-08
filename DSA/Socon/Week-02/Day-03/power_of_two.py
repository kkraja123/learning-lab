# 231. Power of Two
# https://leetcode.com/problems/power-of-two/description/

# Input: n = 16
# Output: true
# Explanation: 24 = 16


class Solution:

    def isPowerOfTwo(self, n: int) -> bool:

        if n == 1:
            return True
        if n <= 0 or n % 2 != 0:
            return False
        return self.isPowerOfTwo(n / 2)


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPowerOfTwo(3)) # O(log n) & O(log n)
