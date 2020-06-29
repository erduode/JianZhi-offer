'''
二叉树中的最大路径和
'''

from Sorting_and_searching.Tree_num1 import Tree

class Solution(Tree):
    def __init__(self):
        super(Solution, self).__init__()
        self.result = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.getMax(root)
        return self.result

    def getMax(self, root):
        """辅助函数"""

        # 如果当前节点为空就表示包含当前节点的最大路径为0
        if root == None:
            return 0

        # 递归的计算当前节点的左子树和右子树能提供的最大路径和。如果为负，就置为0（相当于从头开始）
        left = max(0, self.getMax(root.left))
        right = max(0, self.getMax(root.right))

        # 注意：最长的路径肯定是属于从一端的最左侧到这端的最右侧的一部分
        # 每计算一次左右子树的最大值，就更新当前的result
        self.result = max(self.result, left + right + root.val)

        # 回溯到父节点，最大路径就只能包含左右两个子树中的一个
        return max(left, right) + root.val

    def maxPathSum1(self, root):
        # float('-inf')表示负无穷
        self.res = float('-inf')
        def getMax(root):
            if root is None:
                return 0
            left = max(0, self.getMax(root.left))
            right = max(0, self.getMax(root.right))
            self.res = max(self.res, left + right + root.val)
            return max(left, right) + root.val
        getMax(root)
        return self.res


if __name__ == '__main__':
    datas = [1, -3, 4, 6, 9, 12, -6]
    tree = Solution()  # 新建一个树对象
    for data in datas:
        tree.add(data)  # 逐个加入树的节点
    print(tree.maxPathSum1(tree.root))
