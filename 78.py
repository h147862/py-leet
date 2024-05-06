# 78. Subsets
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]
        temp = []
        self.sub(nums, res, temp)
        return res
    
    def sub(self, nums: list[int], res: list[list[int]] , temp: list[int]):
        if len(nums) < 1:
            return
        for idx, t in enumerate(nums):
            temp.append(t)
            res.append(temp[:])
            self.sub(nums[idx+1:], res, temp)
            temp.pop()


        
if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    res = s.subsets(nums)
    print(res)