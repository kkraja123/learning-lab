# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/description/

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

class Solution:

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        start = end = sums = 0
        count = float('inf')

        for end in range(len(nums)):

            new_count = 0
            
            sums += nums[end]

            while sums>=target:
                count = min(count, end - start + 1)
                sums -= nums[start]
                start+=1

        return 0 if count == float('inf') else count


if __name__ == "__main__":
    solution = Solution()
    print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))  # O(n) & O(1)
