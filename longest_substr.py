"""
Created on Mon Oct 26 22:03:05 2020
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: MEDIUM

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = [0]
        l = ""
        for i in s:
            if i not in l:
                l += i
                d.append(len(l))
            else:
                d.append(len(l))
                l = l[l.index(i) + 1:] + i
        return max(d)
