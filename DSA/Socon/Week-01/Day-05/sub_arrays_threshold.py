# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).


class Solution:

    def numOfSubarraysSumTwoPointer(self, arr, k, threshold):

        start = 0
        count = 0
        size = k

        while k <= len(arr):
            sums = sum(arr[start:k])
            if sums / size >= threshold:
                count += 1
            start += 1
            k += 1
        return count

    def numOfSubarraysOptimized(self, arr, k, threshold):

        start = 0
        count = 0
        size = k
        sums = sum(arr[start:k])

        while k <= len(arr):

            if sums / size >= threshold:
                count += 1
            if k < len(arr):
                sums = sums - arr[start] + arr[k]
            start += 1
            k += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.numOfSubarraysSumTwoPointer([2, 2, 2, 2, 5, 5, 5, 8], 3, 4)
    )  # O(nk) & O(k)
    print(
        solution.numOfSubarraysOptimized([2, 2, 2, 2, 5, 5, 5, 8], 3, 4)
    )  # O(n) & O(k)
