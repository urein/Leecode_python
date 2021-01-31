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
        用一个dict保存已经遍历过的元素，key是元素值，value是该元素的索引。
        对于当前遍历的元素n，在dict中查找 diff=target-n 是否存在，如果存在则直接返回n和diff的索引，
        否则将n记录在dict中。
        在基于hash表的dict中查找元素的时间复杂度是O(1)：空间换时间
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





