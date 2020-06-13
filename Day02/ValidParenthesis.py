'''

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(': ')', '[': ']', '{': '}'}

        stack = []
        for c in s:
            if c in dic:
                stack.append(c)
            else:
                if stack:
                    top = stack.pop()
                    print(dic[top])
                    if c != dic[top]:
                        return False
                else:
                    return False
        # 在python中 None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False
        return not stack

if __name__ == '__main__':
    s = Solution()
    v = s.isValid("[]")
    print(v)