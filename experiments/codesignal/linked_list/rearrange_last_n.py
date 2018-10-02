# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
from utils import convertArrayToList, Node, printList

def rearrangeLastN(l, n):
    if n == 0:
        return l
    i = 1
    node = l
    nth = l
    prev = None
    prev2 = None
    while node != None:
        if i > n:
            prev = nth
            nth = nth.next
        i += 1
        prev2 = node
        node = node.next
    if not prev:
        # first node
        return l
    prev.next = None
    prev2.next = l
    l = nth
    return l


def main():
    head = convertArrayToList([1,2,3,4,5,6,7])
    head = rearrangeLastN(head, 3)
    printList(head)

if __name__ == '__main__':
    main()
