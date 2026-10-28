# 566. Reshape the Matrix
# https://leetcode.com/problems/reshape-the-matrix/description/

# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]


from typing import List


class Solution:

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        m = len(mat)
        n = len(mat[0])

        print(m,n)

        if m * n != r * c:
            return mat

        new_mat = [[0] * c for _ in range(r)]

        arr = []
        index = 0

        for i in range(m):
            for j in range(n):
                arr.append(mat[i][j])

        for k in range(r):
            for l in range(c):
                new_mat[k][l] = arr[index]
                index += 1

        return new_mat


if __name__ == "__main__":
    solution = Solution()
    print(solution.matrixReshape([[1, 2], [3, 4]], 1, 4))  # O(mn) & O(mn + rc) need optimize