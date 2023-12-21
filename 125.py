# https://leetcode.com/problems/valid-palindrome/
# 125. Valid Palindrome
# Easy
# 8.6K
# 8.1K
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s) -1
        i = 0
        while i < j:
            if s[i].isalnum():
                l = s[i].lower()
            else: 
                i+=1
                continue
            if s[j].isalnum():
                r = s[j].lower()
            else: 
                j-=1
                continue
            if l != r:
                return False
            i+=1
            j-=1
        return True

if __name__ == '__main__':
    s = Solution()
    t = "A man, a plan, a canal: uanama"
    res = s.isPalindrome(t)
    print(res)