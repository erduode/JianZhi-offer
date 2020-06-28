'''
 二叉树的最大深度
'''


class TreeNode:
    def __init__(self, x = -1):
        self.val = x
        self.left = None
        self.right = None


class Tree():
    # 树类
    def __init__(self):
        self.root = TreeNode()

    def add(self, data):
        # 为树加入节点
        node = TreeNode(data)
        if self.root.val == -1:  # 如果树为空，就对根节点赋值
            self.root = node
        else:
            myQueue = []
            treeNode = self.root
            myQueue.append(treeNode)
            while myQueue:  # 对已有的节点进行层次遍历
                treeNode = myQueue.pop(0)
                if not treeNode.left:
                    treeNode.left = node
                    return
                elif not treeNode.right:
                    treeNode.right = node
                    return
                else:
                    myQueue.append(treeNode.left)
                    myQueue.append(treeNode.right)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        # 关于为什么返回值为整数：因为上一句，root不存在返回0，所以叶子结点因为下面的语句+1返回1
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1
        return max(left, right)


if __name__ == '__main__':
    datas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = Tree()  # 新建一个树对象
    for data in datas:
        tree.add(data)  # 逐个加入树的节点

    print(tree.maxDepth(tree.root))
