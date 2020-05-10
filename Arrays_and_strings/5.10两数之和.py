'''
两数之和
'''

class Solution:
    # 第一种方法：两个循环
    def sum(self,nums,target):
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if nums[j] == (target - nums[i]):
                    return [i,j]
        return None

    # 第二种方法：利用枚举函数enumerate（可以同时获得下标和值）
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None


if __name__ == '__main__':

    nums = [2,5,5,11]
    target = 10
    s = Solution()
    result = s.sum(nums,target)
    print(result)
    # spam = ['cat', 'dog', 'mouse']
    # s = len(spam)
    # for i in range(s):
    #     print(spam[i])