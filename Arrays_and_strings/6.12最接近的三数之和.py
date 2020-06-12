'''
最接近的三数之和
示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
'''

class Solution:
    def threeSumClosest(self, nums, target):
        mindiff = 10000
        nums.sort()
        res = 0
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                diff = abs(sum - target)
                if diff < mindiff:
                    mindiff = diff
                    res = sum
                if target == sum:
                    return sum
                elif sum > target:
                    right = right - 1
                else:
                    left = left + 1
        return res

if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    s = Solution()
    res = s.threeSumClosest(nums,target)
    print(res)