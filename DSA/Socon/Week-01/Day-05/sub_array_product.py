# 713. Subarray Product Less Than K
# https://leetcode.com/problems/subarray-product-less-than-k/description/

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.


class Solution:

    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        start, end, product, count = 0, 0, 1, 0

        if k <= 1:
            return 0

        while end < len(nums):
            product *= nums[end]

            while product >= k:
                product //= nums[start]
                start += 1
            if product < k:
                count += end - start + 1
            end += 1
        return count
    
    def numSubarrayProductOptimized(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
            
        start, product, count = 0, 1, 0

        for end in range(len(nums)):
            product *= nums[end]

            while product >= k:
                product//=nums[start]
                start+=1
            
            count+=end - start + 1
            
        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100)) # O(n) & O(1)
    print(solution.numSubarrayProductOptimized([10, 5, 2, 6], 100))
