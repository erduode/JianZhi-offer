'''
多数元素
'''

class Solution:
    # 哈希表法
    def majorityElement(self, nums):
        dic = {}
        length = len(nums)
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        for k, v in dic.items():
            if v > length/2:
                return k

    # 排序法
    def majorityElement1(self,nums):
        nums.sort()
        return nums[len(nums)//2]


if __name__ == '__main__':
    nums =[2,2,1,1,1,2,2]
    s = Solution()
    res = s.majorityElement(nums)
    print(res)
