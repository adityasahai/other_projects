from utils import convertArrayToList, Node, printList, countNodes

def partition(head, value):
    if not head:
        return head
    cur = head
    prev = None
    newHead = Node(0)
    n = newHead
    while cur != None:
        node = None
        if cur.value >= value:
            node = cur
            if prev:
                prev.next = node.next
                cur = node.next
            else:
                head = head.next
                cur = head
            node.next = None
            n.next = node
            n = node
        else:
            prev = cur
            cur = cur.next
    if prev:
        prev.next = newHead.next
        return head
    else:
        return newHead.next

def partition2(head, value):
    left, right = Node(0), Node(0)
    l, r = left, right
    while head != None:
        if head.value < value:
            l.next = head
            l = l.next
        else:
            r.next = head
            r = r.next
        head = head.next
    l.next = right.next
    r.next = None
    return left.next

def main():
    head = convertArrayToList([1,2,3,4])
    head = partition2(head, 0)
    printList(head)

if __name__ == '__main__':
    main()