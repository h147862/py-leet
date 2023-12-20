# https://leetcode.com/problems/valid-anagram/
# 242. Valid Anagram
# Easy
# 11.4K
# 359
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = {}
        td = {}
        for idx, c in enumerate(s):
            sd[c] = sd.get(c, 0) +1
            td[t[idx]] = td.get(t[idx], 0) +1
        return sd == td

if __name__ == '__main__':
    a ="a"
    b ="ab"
    s = Solution()
    res = s.isAnagram(a, b)
    print(res)