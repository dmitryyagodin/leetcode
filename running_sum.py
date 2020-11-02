"""
Created on Tue Oct 27 11:30:22 2020
https://leetcode.com/problems/running-sum-of-1d-array/
Difficulty: EASY
10/27/2020 11:35
"""
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # uses list comprehension and enumerate function
        return [v + sum(nums[:i]) for i,v in enumerate(nums)]

z = Solution()
nums = [3,1,2,10,1]
print(z.runningSum(nums))
