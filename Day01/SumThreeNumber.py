'''
三数之和
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sortnums = nums.sort()
        return sortnums

if __name__ == '__main__':
    nums = [1, 2, -1, -3, 0]
    solu = Solution.threeSum(nums)
    print(solu)