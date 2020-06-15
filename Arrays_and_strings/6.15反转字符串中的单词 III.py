'''
反转字符串中的单词 III
示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc"
'''

class Solution:
    def reverseWords(self, s):
        temp = ""
        j = 0
        if s == "":
            return s
        for i in range(len(s)):
            if s[i] == " ":
                temp = temp + s[j:i][::-1] + " "
                j = i + 1
            elif i == len(s) - 1:
                temp = temp + s[j:i+1][::-1]
                return temp

if __name__ == '__main__':
    str = "Let's take LeetCode contest"
    s = Solution()
    res = s.reverseWords(str)
    print(res)