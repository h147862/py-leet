# https://leetcode.com/problems/top-k-frequent-elements/
# 347. Top K Frequent Elements
# Medium
# 16.4K
# 602
# Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        lookup = {}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i] = 1
        for n, f in freq.items():
            if f not in lookup:
                lookup[f]= [n]
            else:
                lookup[f].append(n)
        sortedFreq = sorted(list(lookup.keys()), reverse= True)
        res = []
        if len(sortedFreq) == 0:
            return nums
        flag = True
        while flag:
            for most in sortedFreq:
                if flag:
                    for n in lookup[most]:
                        if k == 0:
                            flag = False
                            break
                        res.append(n)
                        k-=1
                else:
                    break
        return res

if __name__ == '__main__':
    s = Solution()
    t = [1,1,1,2,2,2,3,3,3]
    res = s.topKFrequent(t, 3)
    print(res)