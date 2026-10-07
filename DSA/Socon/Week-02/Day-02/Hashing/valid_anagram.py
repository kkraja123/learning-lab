# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/

# Input: s = "anagram", t = "nagaram"
# Output: true


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}
        freqt = {}

        if len(s) != len(t):
            return False

        for ch in s:
            if ch in freqs:
                freqs[ch] += 1
            else:
                freqs[ch] = 1

        for ch in t:
            if ch in freqt:
                freqt[ch] += 1
            else:
                freqt[ch] = 1

        for i in s:

            if i not in freqt:
                return False

            if freqs[i] != freqt[i]:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram")) # O(n) & O(n)
