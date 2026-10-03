# Max Sum Subarray of size K
# https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

# Input: arr[] = [100, 200, 300, 400], k = 2
# Output: 700
# Explanation: arr2 + arr3 = 700, which is maximum.


class Solution:

    def maxSubarraySumTwoPointer(self, arr, k):
        start = 0
        maxi = 0

        while k <= len(arr):

            sums = sum(arr[start:k])

            if sums > maxi:
                maxi = sums

            start += 1
            k += 1

        return maxi

    def maxSubarraySumOptimized(self, arr, k):
        # code here

        start = 0

        window_sum = sum(arr[:k])
        maxi = window_sum

        for end in range(k, len(arr)):

            window_sum = window_sum - arr[start] + arr[end]

            if window_sum > maxi:
                maxi = window_sum

            start += 1

        return maxi


if __name__ == "__main__":
    arr = [100, 200, 300, 400]
    k = 2
    solution = Solution()
    print(solution.maxSubarraySumTwoPointer(arr, k)) # O(nk) & O(k)
    print(solution.maxSubarraySumOptimized(arr, k)) # O(n) & O(1)
