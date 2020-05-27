'''
最长公共前缀
示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
'''

class Solution:
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ""
        str_minlen = len(strs[0])
        for i in range(len(strs)):#算出此数组中最短的那个字符串的长度
            if len(strs[i]) < str_minlen:
                str_minlen = len(strs[i])
        result = ""
        for i in range(str_minlen):
            target = strs[0][i]#取第一个字符串的第i个字母作为比对的标准
            for j in range(len(strs)):#对每一个字符串的第i个字母进行比对
                if strs[j][i] != target:
                    return result
            result = result + target
        return result

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    s = Solution()
    result = s.longestCommonPrefix(strs)
    print(result)



