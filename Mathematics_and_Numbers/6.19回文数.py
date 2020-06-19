'''
回文数
示例 1:

输入: 121
输出: true
'''

class Solution:
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False

    # 进阶
    def isPalindrome1(self, x):
        num = 0
        temp = x
        while temp != 0:
            num = num*10 + temp%10
            temp = temp // 10
        if num == x:
            return True
        else:
            return False

if __name__ == '__main__':
    x = 121
    s = Solution()
    res = s.isPalindrome1(x)
    print(res)