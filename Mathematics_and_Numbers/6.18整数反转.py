'''
Mathematics and Numbers
'''

class Solution(object):
    # 方法一：转变成字符串操作
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 判断是否为个位数，是个位数则不用反转，直接返回
        if -10 < x < 10:
            return x
        # 把整数x转为字符串
        str_x = str(x)
        # 判断第一个是否为负号
        if str_x[0] != "-":
            # 不是负号则直接反转
            str_x = str_x[::-1]
            # str转为int
            x = int(str_x)
        else:
            # 是负号，则反转负号之后的字符串
            str_x = str_x[1:][::-1]
            # str转int
            x = int(str_x)
            # 加上负号
            x = -x
        # 三目运算符，判断是否溢出
        # 如果-2147483648 < x < 2147483647则返回x，否则返回0
        return x if -2**31 < x < 2**31 else 0

    # 方法二：
    def reverse1(self, x):
        num = 0
        if x == 0:
            return 0
        elif x < 0:
            x = -x
            while x != 0:
                num = num*10 + x%10
                x = x // 10
                num = -num
        else:
            while x != 0:
                num = num*10 + x%10
                x = x // 10
        if num > pow(2, 31) - 1 or num < pow(-2, 31):
            return 0
        return num

if __name__ == '__main__':
    s = Solution()
    reverse_int = s.reverse(-120)
    print(reverse_int)