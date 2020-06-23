'''
排序链表
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 归并排序
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        mid = self.git_mid(head)
        l = head
        r = mid.next
        mid.next = None
        return self.merge(self.sortList(l), self.sortList(r))

    def merge(self, p, q):
        tem = ListNode(0)
        h = tem
        while q and p:
            if p.val > q.val:
                h.next = q
                q = q.next
            else:
                h.next = p
                p = p.next
            h = h.next
        if p:
            h.next = p
        if q:
            h.next = q
        return tem.next

    # 快慢指针的妙用，快指针步进两格，慢指针步进一格
    def git_mid(self, node):
        if node is None:
            return node
        fast = slow = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # 方法二：转变成列表排序，在变成链表
    def sortList1(self, head: ListNode) -> ListNode:
        stack = list()
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next

        stack.sort()
        temp = head
        for index in stack:
            temp.val = index
            temp = temp.next
        return head

if __name__ == '__main__':
    s = Solution()
