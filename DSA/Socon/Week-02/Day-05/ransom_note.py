# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/description/

# Input: ransomNote = "aa", magazine = "aab"
# Output: true


from collections import Counter


class Solution:

    def canConstruct(self, ransomNote, magazine):

        rans = {}
        mags = {}

        for i in ransomNote:
            if i in rans:
                rans[i] += 1
            else:
                rans[i] = 1

        for i in magazine:

            if i in mags:
                mags[i] += 1
            else:
                mags[i] = 1

        for i in ransomNote:

            if i not in mags:
                return False

            print(mags[i], rans[i])

            if mags[i] < rans[i]:
                return False

        return True

        # n= len(ransomNote)
        # count = Counter(magazine)
        # for i in range(n):
        #     if count[ransomNote[i]] == 0:
        #         return False
        #     count[ransomNote[i]] -= 1
        # return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.canConstruct("fihjjjjei", "hjibagacbhadfaefdjaeaebgi"))  #
