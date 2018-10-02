from utils import convertArrayToList, Node, printList, countNodes

def removeNthFromEnd2(head, n):
    node = head
    prev = None
    nth = head
    i = 1
    while node != None:
        if i > n:
            prev = nth
            nth = nth.next
        i += 1
        node = node.next
    if not prev:
        # first node
        nth = nth.next
        return nth
    if not nth:
        # last node
        prev.next = None
        return head
    prev.next = nth.next
    return head

def removeNthFromBegining(head, n):
    node = head
    prev = None
    i = 1
    while i != n:
        prev = node
        node = node.next
        i = i + 1
    if not prev:
        # first node
        node = node.next
        return node
    if not node:
        # last node
        prev.next = None
        return head
    prev.next = node.next
    return head




def removeNthFronEnd(head, n):
    N = countNodes(head)
    return removeNthFromBegining(head, N - n + 1)

def main():
    head = convertArrayToList([1,2,3,4,5])
    # head = removeNthFromBegining(head, 2)
    head = removeNthFronEnd(head, 2)
    printList(head)
    # head = convertArrayToList([1])
    # head = removeNthFromBegining(head, 1)
    # printList(head)
    head = convertArrayToList([1,2])
    head = removeNthFronEnd(head, 2)
    printList(head)
    head = convertArrayToList([1,2,3,4,5])
    head = removeNthFromEnd2(head, 2)
    printList(head)

if __name__ == '__main__':
    main()
