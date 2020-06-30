'''
二叉搜索树的最近公共祖先

思路
关键点是二叉搜索树，研究发现有如下规律。

如果p，q一个大于根节点，一个小于根节点，那么p，q的最近公共祖先就是根节点。
如果p，q都小于根节点，则令root=root.left；
如果p，q都大于根节点，则令root=root.right；
继续判断，直到某节点位于p，q之间。

'''
from Sorting_and_searching.Tree_num1 import Tree

class Solution(Tree):
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if q.val > root.val and p.val > root.val:
                root = root.right
            elif q.val < root.val and p.val < root.val:
                root = root.left
            else:
                break
        return root

if __name__ == '__main__':
    datas = [1, -3, 4, 6, 9, 12, -6]

    tree = Solution()  # 新建一个树对象
    for data in datas:
        tree.add(data)  # 逐个加入树的节点
    p = tree.root.left
    q = tree.root.right
    print(tree.lowestCommonAncestor(tree.root, p, q).val)