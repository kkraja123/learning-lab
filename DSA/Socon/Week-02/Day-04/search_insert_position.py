# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/description/

# Input: nums = [1,3,5,6], target = 5
# Output: 2


class Solution:

    def searchInsert(self, nums: list[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return l


if __name__ == "__main__":
    solution = Solution()
    print(solution.searchInsert([1, 3, 5, 6], 5))  #O(log n)
