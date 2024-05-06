# https://leetcode.com/problems/valid-parentheses/
# 20. Valid Parentheses
# Easy
# 22.9K
# 1.6K
# Companies
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        tmp = []
        for c in s:
            if c not in [']',')','}']:
                tmp.append(c)
            else:
                if len(tmp)>0:
                    t = tmp.pop()
                    if t+c not in ['()', '[]', '{}']:
                        return False
                else:
                    return False
        if len(tmp) > 0:
            return False
        return True



if __name__ == '__main__':
    s = Solution()
    t = "()"
    res = s.isValid(t)
    print(res)