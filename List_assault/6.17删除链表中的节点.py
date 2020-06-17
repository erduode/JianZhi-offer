'''
删除链表中的节点

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3

    n1.deleteNode(n2)
    print(n2.val)