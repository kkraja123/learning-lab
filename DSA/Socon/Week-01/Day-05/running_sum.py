# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/description/

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


class Solution:

    def runningSumWithArray(self, nums):

        arr = []
        sum = 0

        for i in range(len(nums)):
            sum = sum + nums[i]
            arr.append(sum)
        return arr

    def runningSumOptimized(self, nums):

        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums


if __name__ == "__main__":
    solution = Solution()
    print(solution.runningSumOptimized([1, 2, 3, 4]))  # O(n) & O(1)
    print(solution.runningSumWithArray([1, 2, 3, 4]))  # O(n) & O(n)
