# LCM -  Least Common Multiple

# The LCM of two numbers is the smallest positive number that is evenly divisible by both of them.

# https://www.geeksforgeeks.org/problems/lcm-of-two-numbers/1

from gcd import Solution as GCDSolution

class Solution:

    def lcmEveryElement(self, a, b):
        maxi = max(a, b)
        while True:
            if maxi % a == 0 and maxi % b == 0:
                return maxi

            maxi = maxi + 1

    def lcmOnlyMultipls(self, a, b):
        muliple = a

        while muliple % b != 0:
            muliple = muliple + a
        return muliple
    
    def lcmOptimized(self, a, b):
         gcdSolution = GCDSolution()
         gcd  = gcdSolution.gcdEuclidean(a,b)
         return (a*b)//gcd

if __name__ == "__main__":
    solution = Solution()
    print(solution.lcmEveryElement(12, 18)) # O(a × b) & O(1)
    print(solution.lcmOnlyMultipls(18, 12)) # O(b / GCD(a,b)) & O(1)
    print(solution.lcmOptimized(18, 12)) # O(log(min(a,b))) & O(log(min(a,b)))
