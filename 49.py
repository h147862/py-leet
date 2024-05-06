# https://leetcode.com/problems/group-anagrams/
# 49. Group Anagrams
# Medium
# 17.8K
# 531
# Companies
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.




class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
       
        group = {}
        for s in strs:
            k = ''
            for c in sorted(list(s)):
                k=k+c
            if k not in group:
                group[k] = [s]
            else:
                group[k].append(s)
        return list(group.values())


if __name__ == '__main__':
    s = Solution()
    t =  ["eat","tea","tan","ate","nat","bat"]
    res = s.groupAnagrams(t)
    print(res)