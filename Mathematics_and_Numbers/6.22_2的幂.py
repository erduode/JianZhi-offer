'''
2的幂
'''


class Solution():
    '''
    方法一（位运算）
    思路
    若n为2的整数，不妨设其为2i
    则其二进制码必为100…0(i个0)
    故n-1为11…1(i个1)
    则n&(n-1)为0
    即若n&(n-1)不为0，必不是2的幂
    '''
    def isPowerOfTwo(self, n):
        if n < 0:
            return False
        return n&(n-1) == 0

    '''
    方法二（递归）
    
    '''
    def isPowerOfTwo1(self, n):
        if n == 1:
            return True
        elif n <= 0 or n%2 == 1:
            return False
        else:
            return self.isPowerOfTwo1(n/2)




if __name__ == '__main__':
    n = 16
    s = Solution()
    res = s.isPowerOfTwo1(n)
    print(res)