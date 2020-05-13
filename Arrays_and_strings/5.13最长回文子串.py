'''
最长回文子串:
给定一个字符串 s，找到 s 中最长的回文子串。

示例 1：

输入: "babad"
输出: "bab"
'''

class Solution():
    # 方法一：
    def longestPalindrome(self,s):
        max_len = 0
        result = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s)+1):
                # 1、切片！
                # 2、s[i:j:-1]与s[i:j][::-1]的区别：(知识点)
                #    s[i:j][::-1] == s[i:j]逆序
                #    s[i:j:-1]一般不用，i表示倒着数的第一个数，j表示倒着数的最后一个数
                a = s[i:j]
                b = s[i:j][::-1]
                if s[i:j] == s[i:j][::-1]:
                    if max_len < j - i:
                        max_len = j - i
                        result = s[i:j]
        return result

# b = a[i:j:s] #表示：i,j与上面的一样，但s表示步进，缺省为1.
# 所以a[i:j:1]相当于a[i:j]
# 当s<0时，i缺省时，默认为-1. j缺省时，默认为-len(a)-1
# 所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍，即倒序。



if __name__ == '__main__':
    str = "rwr"
    s = Solution()
    result = s.longestPalindrome(str)
    print(result)


