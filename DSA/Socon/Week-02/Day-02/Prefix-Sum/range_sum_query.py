# 303. Range Sum Query - Immutable
# https://leetcode.com/problems/range-sum-query-immutable/description/

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

class Solution:

    prefix_sum = []

    def __init__(self, nums: list[int]):
        self.prefix_sum = nums
        for i in range(1, len(nums)):
            self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        
        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right] - self.prefix_sum[left-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.sumRange([[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]])) # can't run in vs code. 