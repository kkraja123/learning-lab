# Prime Number

# The number should divisable by 1 and itself
# 0 and 1 has only one divisable so it is not prime



class Solution:
    
    # https://www.geeksforgeeks.org/problems/prime-number2314/1
    def isPrime(self, n):
        # code here
        if (n <= 1):
            return False

        # i = 2

    #    while (i<n):  O(n)
        for i in range(2, int(n**0.5) + 1): #O(root n) optimized

            if (n % i == 0):
                return False
            
        return True

# Sieve Of Eratosthenes

# find how many prime number in given n

# https://leetcode.com/problems/count-primes/submissions/2156392510/

    def countOfPrime(self, n):

        output = [True] * n

        if n <= 2:
            return 0

        output[0] = False
        output[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            
            if(output[i]):
                for k in range(i*i, n, i):
                    output[k] = False
                
        return output.count(True)   
        
n = 3452593
if __name__ == "__main__":
    solution = Solution()

    print(solution.isPrime(n)) # O(√n) & O(1)
    print(solution.countOfPrime(n)) # O(n log log n) & O(n)
