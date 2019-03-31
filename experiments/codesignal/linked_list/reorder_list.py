from utils import *

def reorderList(head):
    if not head or not head.next:
        return head

    # find the middle of the list
    p1 = head
    p2 = head
    while p2.next and p2.next.next:
        p1 = p1.next
        p2 = p2.next.next
    
    # reverse the second half of the list
    preMiddle = p1
    preCurrent = p1.next
    while preCurrent.next:
        current = preCurrent.next
        preCurrent.next = current.next
        current.next = preMiddle.next
        preMiddle.next = current

    printList(head)
    print("_____")

    # start reorder one by one
    p1 = head
    p2 = preMiddle.next
    while p1 != preMiddle:
        preMiddle.next = p2.next
        p2.next = p1.next
        p1.next = p2
        p1 = p2.next
        p2 = preMiddle.next
    
    return head


def main():
    head = convertArrayToList([1,2,3,4,5,6,7,8,9])
    head = reorderList(head)
    printList(head)

if __name__ == '__main__':
    main()