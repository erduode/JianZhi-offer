'''
盛最多水的容器
示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49
'''

'''
思路

双指针法，一个放在开头，一个放在结尾，面积就是两个索引中较短的长度*双指针之间的距离，
每次更新显然是要把较短的那端向另一头移动，这样较有可能使得面积更大
'''

class Solution:
    def maxArea(self, height):
        '''
        :type height:List[int]
        :rtype:int
        '''
        l = 0
        r = len(height) - 1
        s = 0
        while l < r:
            s = max(s, (r - l) * min(height[l], height[r]))
            if height[l] > height[r]:
                r = r - 1
            else:
                l = l + 1
        return s

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    s = Solution()
    res = s.maxArea(height)
    print(res)