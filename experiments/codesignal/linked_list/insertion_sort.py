from utils import *

def insertNode(head, node):
    if not head:
        head = node
        node.next = None
    else:
        n = head
        prev = None
        while n and n.value < node.value:
            prev = n
            n = n.next
        if not prev:
            # insert at top
            node.next = head
            head = node
        else:
            node.next = n
            prev.next = node
    return head

def insertionSort(head):
    newList = None
    while head:
        n = head.next
        newList = insertNode(newList, head)
        head = n
    return newList
        
def testInsertNode():
    head = convertArrayToList([1])
    printList(insertNode(head, Node(2)))

def main():
    head = convertArrayToList([-1, 5, 3, 4, 0])
    # insertionSort(head)
    printList(insertionSort(head))

if __name__ == '__main__':
    main()
    # testInsertNode()
