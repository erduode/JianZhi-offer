'''
字符串转换整数

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

    1、如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
    2、假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
    3、该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
'''


class Solution():
    def myAtoi(self, str):
        str = str.strip()
        if str == "":
            return 0
        # 用于解决越界
        elif str[0] == "+" or str[0] == "-":
            # 用于解决越界
            if str == "+" or str == "-":
                return 0
            else:
                if str[1] <= "9" and str[1] >= "0":
                    for i in range(1, len(str)):
                        if str[i] >= "0" and str[i] <= "9":
                            str1 = str[:i + 1]
                        else:
                            break
                    intg = int(str1)
                    if intg >= -2147483648 and intg <= 2147483647:
                        return intg
                    elif intg > 2147483647:
                        return 2147483647
                    else:
                        return -2147483648
                else:
                    return 0

        elif str[0] <= "9" and str[0] >= "0":
            for i in range(len(str)):
                if str[i] >= "0" and str[i] <= "9":
                    str1 = str[:i + 1]
                else:
                    break
            intg = int(str1)
            if intg >= -2147483648 and intg <= 2147483647:
                return intg
            elif intg > 2147483647:
                return 2147483647
            else:
                return -2147483648
        else:
            return 0


if __name__ == '__main__':
    str = "3.14159"
    s = Solution()
    result = s.myAtoi(str)
    print(result)

