# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/2158576696/

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].


class Solution:

    #Brute-Fore 
        # need to do

    # Two Pointer
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        start = 0
        end = len(numbers) - 1

        while start < end:
            sums = numbers[start] + numbers[end]
            if sums == target:
                return [start + 1, end + 1]
            elif sums < target:
                start += 1
            else:
                end -= 1

if __name__ == "__main__":
    arr = [2,7,11,15]
    target = 9
    solution = Solution()
    print(solution.twoSum(arr,target)) # O(n) & O(1)

