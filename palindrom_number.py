"""
Problem:
    Determine whether an integer is a palindrome.
    An integer is a palindrome when it reads the same backward as forward.
Source:
    https://leetcode.com/problems/palindrome-number/
Difficulty: EASY

Example:
    Input: x = 121          Input: x = -101
    Output: true            Output: false

Sumbission detail:
    https://leetcode.com/submissions/detail/414858705/

Date: Oct 30, 2020
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # for intputs of less than 4 digits just compare the first and the last
        if len(str(x)) < 4:
            return str(x)[0] == str(x)[-1]
        # in other cases compare them recursively reducing the input on both sides
        else:
            if str(x)[0] == str(x)[-1]:
                return self.isPalindrome(str(x)[1:-1])
