'''
二叉搜索树中第K小的元素
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 中序遍历迭代法
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        :param root: TreeNode
        :param k: int
        :return: int
        """
        result = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                if len(result) >= k:
                    break

                root = root.right
        return result[k-1]

    # 未完待续。。（中序遍历递归）