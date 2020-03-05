'''
螺旋矩阵
'''


class Solution:
    def generateMatrix(self,matrix: [[int]]):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if matrix == 0:
            return matrix
        res = []
        br = 0
        er = len(matrix) - 1 # 行数
        bc = 0
        ec = len(matrix[0]) - 1 # 列数
        while 1:
            i1 = bc
            while i1 <= ec:
                res.append(matrix[br][i1])
                i1 = i1 + 1
            br += 1
            if br > er:
                break

            i2 = br
            while i2 <= er:
                res.append(matrix[i2][ec])
                i2 = i2 + 1
            ec -= 1
            if ec < bc:
                break

            i3 = ec
            while i3 >= bc:
                res.append(matrix[er][i3])
                i3 = i3 - 1
            er -= 1
            if er < br:
                break

            i4 = er
            while i4 >= br:
                res.append(matrix[i4][bc])
                i4 = i4 - 1
            bc += 1
            if bc > ec:
                break
        return res


if __name__ == '__main__':
    # z = [[7 for i in range(10)] for j in range(10)]
    # print(z)
    # x=y=0
    # xoy = [x][y]
    # print(xoy)
    list = [
             [ 1, 2, 3 ],
             [ 4, 5, 6 ],
             [ 7, 8, 9 ]
            ]
    s = Solution()
    s1 = s.generateMatrix(list)
    print(s1)
