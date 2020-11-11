"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


class Solution:
    def two_sum(self, nums: list, target: int):
        for i1, n1 in enumerate(nums[:-1]):
            for i2, n2 in enumerate(nums[i1+1:], i1+1):
                if n1 + n2 == target:
                    return i1, i2


if __name__ == '__main__':
    s = Solution()
    ret = s.two_sum([2, 7, 11, 15, 34, 24, 8, 32], 15)
    print(ret)




