'''
寻找两个正序数组的中位数

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
'''

class Solution():
    def findMedianSortedArrays(self,nums1,nums2):
        nums = nums1 + nums2
        nums = sorted(nums)
        l = len(nums)
        if l % 2 == 0:
            # “/”运算符得到的类型是float，需要强制转换成int
            n1 = int(l / 2 - 1)
            n2 = int(l/2)
            mid = (nums[n1] + nums[n2])/2
        else:
            # 可以用 n3 = (l-1)//2代替下面语句
            n3 = int((l - 1)/2)
            mid = nums[n3]
        return mid

if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [2, 4,3]

    s = Solution()
    result =s.findMedianSortedArrays(nums1,nums2)
    print(result)
