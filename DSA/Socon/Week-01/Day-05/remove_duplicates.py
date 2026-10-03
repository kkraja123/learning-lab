# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


class Solution:

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r, c = 0, 1, 1

        while r < len(nums):
            if nums[l] != nums[r]:
                nums[c] = nums[r]
                c += 1
            l += 1
            r += 1
        return c

    def removeDuplicatesOptimized(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 1

        while r < len(nums):
            if nums[l] != nums[r]:
                nums[l + 1] = nums[r]
                l += 1
            r += 1
        return l + 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # O(n) & O(1)
    print(
        solution.removeDuplicatesOptimized([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    )  # O(n) & O(1)
