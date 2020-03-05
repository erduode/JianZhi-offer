'''

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        p = l1
        q = l2
        while l2 != None:
            if p.val <= q.val and p.nextval >= q.val:
                l2 = l2.next
                q.next = p.next
                p.next = q
                p = q.next
                q = l2
            elif p.next < q.val:
                if p.next == None:
                    p.next = q
                    return l1
                else:
                    p = p.next
            else:
                if q.next == None:
                    q.next = p
                    return l2
                else:
                    q = q.next
        return l1


if __name__ == '__main__':
    l1 = [1,2,4]
    l2 = [1,3,4]
    s = Solution()
    result = s.mergeTwoLists(l1, l2)
    print(result)