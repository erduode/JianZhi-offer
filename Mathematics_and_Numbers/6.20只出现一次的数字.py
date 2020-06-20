'''
只出现一次的数字
'''

'''
异或运算有这样的特性：

交换律：a ^ b == b ^ a

相同数字异或为零：a ^ a == 0

数字异或零为该数字：a ^ 0 == a
'''
class Solution:
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res
if __name__ == '__main__':
    nums = [4,1,2,1,2]
    s = Solution()
    res = s.singleNumber(nums)
    print(res)

