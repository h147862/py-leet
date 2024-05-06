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
        cnt = {}
        lookup = {}
        res = []
        for n in nums:
            if n not in cnt:
                cnt[n] = 1
            else:
                cnt[n]+=1
        for n , freq in cnt.items():
            if freq in lookup:
                lookup[freq].append(n)
            else:
                lookup[freq] = [n]
        s = sorted(list(set(cnt.values())), reverse= True)
        for freq in s:
            for e in lookup[freq]:
                res.append(e)
                k=k-1
                if k==0:
                    return res
if __name__ == '__main__':
    s = Solution()
    t = [1]
    res = s.topKFrequent(t, 1)
    # t = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
    # res = s.topKFrequent(t, 5)
    print(res)