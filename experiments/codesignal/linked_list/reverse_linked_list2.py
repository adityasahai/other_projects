from utils import *

def reverseBetween(head, m, n):
    if m == n:
        return head
    node1 = head
    node2 = head
    prev2 = None
    i = 1
    while node1:
        i += 1
        if i > (n - m + 1):
            prev2 = node2
            node2 = node2.next
        node1 = node1.next
        if i == n:
            break
    node1next = node1.next if node1.next else None
    h, t = reverseList(node2, node1)
    if prev2:
        prev2.next = h
    else:
        head = h
    t.next = node1next
    return head

def reverseList(head, tail):
    lastElement = head
    newList = None
    while head != tail:
        element = head
        head = head.next
        element.next = newList
        newList = element
    tail.next = newList
    newList = tail
    return newList, lastElement


def main():
    head = convertArrayToList([1,2,3,4,5,6])
    printList(reverseBetween(head, 1, 2))


if __name__ == '__main__':
    main()