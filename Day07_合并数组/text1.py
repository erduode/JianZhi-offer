'''

'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]

if __name__ == '__main__':
    s = Solution()
    nums1 = [1,4,5,0,0,0,0]
    nums2 = [2,4,5,6]
    s.merge(nums1,3,nums2,2)
    print(nums1)