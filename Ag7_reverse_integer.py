"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer
range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""


class Solution:
    def reverse_integer(self, x: int):
        x_str = str(x)
        s_rev = ''.join(reversed(x_str))
        if s_rev[-1] == '-':
            ret = -int(s_rev[:-1])
        else:
            ret = int(s_rev)
        return ret


if __name__ == '__main__':
    s = Solution()
    r = s.reverse_integer(-120)
    print(r)