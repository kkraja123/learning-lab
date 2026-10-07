# 724. Find Pivot Index
# https://leetcode.com/problems/running-sum-of-1d-array/description/

# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11


class Solution:

    def pivotIndex(self, nums: list[int]) -> int:

        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.pivotIndex([1,7,3,6,5,6])) 
