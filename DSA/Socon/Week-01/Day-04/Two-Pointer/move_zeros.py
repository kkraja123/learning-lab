# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/description/

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]


class Solution:

    # BruteForce
    # need to do

    # Two-Pointer [0, 1, 0, 3, 12]
    def moveZeroesTwoPointer(self, nums):
        start = 0

        for end in range(len(nums)):
            print(start, end)
            if nums[end] != 0:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1    
        return nums

    # optimized
    def moveZeroesOptimized(self, nums):
        n = len(nums)

        new_arr = [0] * n
        pos = 0

        for j in range(n):
            if nums[j] != 0:
                new_arr[pos] = nums[j]
                pos += 1
        nums[:] = new_arr
        return nums


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]

    solution = Solution()
    # print(solution.moveZeroesOptimized(nums)) # O(n) & O(n)
    print(solution.moveZeroesTwoPointer(nums)) # O(n) & O(1)
