# 643. Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/description/

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75r 

class Solution:

    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        start = 0
        avg = sum(nums[:k])/k
        maxi = avg

        for end in range(k, len(nums)):
            avg = sum(nums[start:end])/k
            maxi = max(avg, maxi)
            start+=1
        return maxi
    
    def findMaxAverageOptimized(self, nums: list[int], k: int) -> float:

        start = 0
        sums = maxi = sum(nums[:k])

        for end in range(k, len(nums)):
            sums = sums - nums[start] + nums[end]
            maxi = max(sums, maxi)
            start+=1
        return maxi/k


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))  # O(nk) & O(k)
    print(solution.findMaxAverageOptimized([1,12,-5,-6,50,3], 4))  # O(n) & O(1)
