"""
Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?


Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:

Input: x = -101
Output: false

"""


class Solution:

    def num_of_digits(self, num: int):
        if num == 0:
            return 1
        num = abs(num)
        n = 0
        while num != 0:
            num //= 10
            n += 1
        return n

    def is_palindrome(self, num: int):
        if num < 0:
            return False
        n_digits = self.num_of_digits(num)
        while n_digits > 1:
            tmp = pow(10, n_digits-1)
            l_bit = num % 10
            h_bit = num // tmp
            if l_bit != h_bit:
                return False
            num = num - tmp * h_bit
            num = num // 10
            n_digits -= 2
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.is_palindrome(21012))
