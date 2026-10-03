#GCD - Greatest Common Divisor

# Greatest Common Divisor (GCD), also known as the Highest Common Factor (HCF), is the greatest number that divides a set of numbers without leaving a remainder.

# For example, GCD of 12 and 18 is 6, as it divides both the numbers and is the largest of all their factors.
# GCD of any two numbers is never negative or 0, and the least positive integer common to any two numbers is always 1.

# https://www.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1

class Solution:
     
    def gcdBrute(self, a, b):
        for i in range(min(a, b), 0, -1):
            if a % i == 0 and b % i == 0:
                return i
            
    def gcdEuclidean(self, a, b):
        factor = a%b
        
        if factor==0:
            return b
        else:
            return self.gcdEuclidean(b,factor)

if __name__ == "__main__":        
    solution = Solution()
    print(solution.gcdBrute(20,30)) # O(min(a,b)) & O(1)
    print(solution.gcdEuclidean(20,30)) # O(log(min(a,b))) & O(log(min(a,b)))
