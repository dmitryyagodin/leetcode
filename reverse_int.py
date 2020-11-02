"""
Given a 32-bit signed integer, reverse digits of an integer.
https://leetcode.com/problems/reverse-integer/
Example:
    Input: x = 123      Input: x = 120  Input: x = -123
    Output: 321         Output: 21      Output: -321

Sumbission detail:
    https://leetcode.com/submissions/detail/415938070/
Date Nov 2, 2020
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < -2147483648 or x > 2147483647 or x == 0:
            return 0

        if x > 0:
            number = int(str(x)[::-1])
        else:
            number = int(str(x)[0] + str(x)[:0:-1])

        if number < -2147483648 or number > 2147483647:
            return 0
        else:
            return number

number = Solution()
print(number.reverse(-123))
