'''
存在重复元素
'''

class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        i=0
        while i < len(nums)-1:
            j = i+1
            while j < len(nums):
                if nums[i] == nums[j]:
                    return True
                else:
                    j = j+1
            i = i+1
        return False

if __name__ == '__main__':
    nums = [1,2,3,3]
    s = Solution()
    is_s = s.containsDuplicate(nums)
    print(is_s)
