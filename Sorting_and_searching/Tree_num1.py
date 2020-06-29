'''
构建树
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

    # 层次遍历加入
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

    def DFS(self, root):  # 递归实现深度优先遍历
        if root == None:
            return
        print(root.val)
        self.DFS(root.left)
        self.DFS(root.right)

