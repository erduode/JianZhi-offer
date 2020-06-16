'''
合并 k 个排序链表
思路：
将所有链表的元素都取出来放在一个list里面.然后使用sorted(list lambda x:x.val) 进行排序,然后进行拼接
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        '''

        :param lists: list
        :return: ListNode
        '''
        templist = []
        for i in lists:
            # 下面这个i是int类型why?
            while i is not None:
                templist.append(i)
                i = i.next

        templist_sorted = sorted(templist, key=lambda n: n.val)
        p = ListNode(-1)
        h = p
        for i in templist_sorted:
            p.next = i
            p = p.next
        p.next = None
        return h.next

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n1.next = n2
    n2.next = n3
    n4.next = n5
    n5.next = n6
    l = [n1, n4]
    s = Solution()
    res = s.mergeKLists(l)
    print(res)
