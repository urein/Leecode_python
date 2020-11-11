"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

from operator import itemgetter


class Solution:

    # def two_sum(self, nums: list, target: int):
    #     """
    #     rude enumeration
    #     """
    #     for i1, n1 in enumerate(nums[:-1]):
    #         for i2, n2 in enumerate(nums[i1+1:], i1+1):
    #             if n1 + n2 == target:
    #                 return i1, i2

    # def two_sum(self, nums: list, target: int):
    #     """
    #     firstly sorting,
    #     then search target in the following way:
    #         left -> <- right
    #     """
    #     idx_num = ([i, v] for i, v in enumerate(nums))
    #     idx_num = sorted(idx_num, key=itemgetter(1))
    #     i1, i2 = 0, len(idx_num)-1
    #     while i1 < i2:
    #         tmp_sum = idx_num[i1][1] + idx_num[i2][1]
    #         if tmp_sum == target:
    #             return idx_num[i1][0], idx_num[i2][0]
    #         elif tmp_sum < target:
    #             i1 += 1
    #         else:
    #             i2 -= 1

    def two_sum(self, nums: list, target: int):
        """
        record searched items in a dict (hash table),
        search (target - n_tmp) from the dict.
        O-complexity of search in a hash-table is O(1)
        trade space for time
        """
        memeory = {nums[0]: 0}
        for idx, n in enumerate(nums[1:], 1):
            diff = target - n
            if diff in memeory:
                return memeory[diff], idx
            memeory[n] = idx


if __name__ == '__main__':
    s = Solution()
    ret = s.two_sum([2, 7, 11, 15, 121, 232, 156, 88], 26)
    print(ret)





