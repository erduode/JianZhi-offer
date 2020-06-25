'''
 数组中的第K个最大元素
'''
import heapq


class Solution:
    # 方法一：自己想的
    def findKthLargest1(self, nums, k):
        nums.sort(reverse=True)
        return nums[k-1]

    # 方法二：利用堆
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # heapq.nlargest(k, nums)输出：前n个最大元素
        return heapq.nlargest(k, nums)[-1]

if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    s = Solution()
    res = s.findKthLargest(nums, k)
    print(res)
