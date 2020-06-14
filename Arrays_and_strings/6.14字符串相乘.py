'''
字符串相乘
输入: num1 = "2", num2 = "3"
输出: "6"
'''

'''
思路：
123*456

100        400
 20         50
  3          6

[3*6, 2*6+3*5, 1*6+2*5+3*4, 2*4+1*5, 1*4, 0]

[18, 27, 28, 13, 4, 0]

[8, 27+1, 28, 13, 4, 0]

[8, 8, 28+2, 13, 4, 0]

[8, 8, 0, 13+3, 4, 0]

[8, 8, 0, 6, 5, 0]

"880650"-->"056088"

"56088"
'''

class Solution:
    def multiply(self, num1, num2):
        '''

        :param num1: str
        :param num2: str
        :return: str
        '''
        num1 = num1[::-1]
        num2 = num2[::-1]
        length1 = len(num1)
        length2 = len(num2)
        # (技巧一）
        temp = [0 for _ in range(length1 + length2)] # 最多是length1 + length2位数(技巧一）
        # 将手算乘法的每列数字放入其格内
        for i in range(length1):
            for j in range(length2):
                # temp[i+j]是重点(技巧二)
                temp[i+j] += int(num1[i]) * int(num2[j])

        ans = []
        for i in range(len(temp)):
            units = temp[i] % 10 # 该位最后的数
            tens = temp[i] // 10 # 进位的数
            if i < len(temp) - 1:
                temp[i+1] += tens
            ans.insert(0, str(units)) # 直接往前写，省的最后反转(技巧三)

        # 删去前面的所有0
        while ans[0] == "0" and len(ans) > 1:
            ans.pop(0)
        return ''.join(ans)




'''
L = [ i**2 for i in range(1,11)]解析语句：将前面的式子一次运算后放入列表
    L = []
    for i in range(1,11):
        L.append(i**2)
'''

if __name__ == '__main__':
    num1 = "123"
    num2 = "456"
    s = Solution()
    res = s.multiply(num1, num2)
    print(res)