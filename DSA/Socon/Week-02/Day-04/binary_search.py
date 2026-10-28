# 704. Binary Search
# https://leetcode.com/problems/binary-search/description/

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4


class Solution:

    def search(self, nums: list[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.search([-1, 0, 3, 5, 9, 12], 9))  #O(log n)
