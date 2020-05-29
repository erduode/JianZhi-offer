'''
三数之和
示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution():
    # 时间太长。。。。但思路简单，复杂度O（n**3）
    def threeSum1(self, nums):
        res = []
        len_num = len(nums)
        for i in range(len_num):
            for j in range(i+1,len_num):
                for k in range(j+1,len_num):
                    tem = [nums[i], nums[j], nums[k]]
                    tem.sort()
                    if  tem not in res:
                        if nums[i] + nums[j] + nums[k] == 0:
                            res.append([nums[i],nums[j],nums[k]])

        return res

    # 参考大神，改进版
    def threeSum2(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[j] + nums[k] + nums[i]
                if sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j = j + 1
                    while j < k and nums[k] == nums[k - 1]:
                        k = k - 1
                    j = j + 1
                    k = k - 1
                elif sum < 0:
                    j = j + 1
                else:
                    k = k - 1
        return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    result = s.threeSum2(nums)
    print(result)
    # nums1 = [[-1, 0, 1], [-1, 2, -1]]
