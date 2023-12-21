# https://leetcode.com/problems/3sum/
# 15. 3Sum
# Medium
# 29.4K
# 2.7K
# Companies
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums = sorted(nums)
        for idx, n in enumerate(nums):
            if idx != 0 and n == nums[idx-1]:
                continue
            s = n
            l = idx +1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + s == 0:
                    res.append([n, nums[l], nums[r]])
                    l = l + 1
                    while nums[l] == nums[l-1] and l < r:
                        l = l + 1
                    continue
                elif  nums[l]+ nums[r] + s > 0:
                    r = r - 1
                    continue
                else:
                    l = l + 1
                    continue
        return res

if __name__ == '__main__':
    s = Solution()
    t = [0,0,0]
    res = s.threeSum(t)
    print(res)