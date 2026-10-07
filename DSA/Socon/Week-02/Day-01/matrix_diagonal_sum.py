# 1572. Matrix Diagonal Sum
# https://leetcode.com/problems/matrix-diagonal-sum/description/

# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.

class Solution:

    def diagonalSum(self, mat: list[list[int]]) -> int:
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.diagonalSum())