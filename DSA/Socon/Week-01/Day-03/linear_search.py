class Solution:

    # Basic Search
    # https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1

    def search(self, arr, x):
        # code here

        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1

    # Find Occurence
    # https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1

    def countFreq(self, arr, target):
        # code here
        occurrence = 0
        for i in range(len(arr)):
            if arr[i] == target:
                occurrence = occurrence + 1
        return occurrence

    # Find min and max
    # https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1
    def findMinMax(self, arr):
        # code here
        mini = arr[0]
        maxi = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < mini:
                mini = arr[i]
            elif arr[i] > maxi:
                maxi = arr[i]
        return [mini, maxi]

    # Reverse the array
    # https://www.geeksforgeeks.org/problems/reverse-an-array/1
    # It is two pointer approch

    def reverseArray(self, arr):
        # code here

        start = 0
        end = len(arr) - 1

        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start = start + 1
            end = end - 1
        return arr

    # Inser a element in particular index
    def insert(self, arr, x, index):
        # code here

        arr.append(0)

        for i in range(len(arr) - 1, index, -1):
            arr[i] = arr[i - 1]
        arr[index] = x
        return arr


arr = [1, 2, 3, 4, 7, 7]
arr1 = [75, 20, 30, 35, 15, 80, 10]
arr2 = [75, 20, 30, 35, 15, 80]
x = 7

if __name__ == "__main__":
    solution = Solution()
    print(solution.search(arr, x)) # O(n) & O(1)
    print(solution.countFreq(arr, x)) # O(n) & O(1)
    print(solution.findMinMax(arr1)) # O(n) & O(1)
    print(solution.reverseArray(arr1)) # O(n) & O(1)
    print(solution.insert(arr2, x, 2)) # O(n) & O(1)
