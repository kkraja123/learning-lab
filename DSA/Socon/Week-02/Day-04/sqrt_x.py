# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/description/

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.


class Solution:

    def mySqrt(self, x: int) -> int:

        start = 1
        end = x

        while start <= end:
            mid = (start + end) // 2
            square = mid * mid

            if square == x:
                return mid

            elif square < x:
                start = mid + 1

            else:
                end = mid - 1

        return end


if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(4))  #
