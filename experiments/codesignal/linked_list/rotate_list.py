from utils import convertArrayToList, Node, printList, countNodes

def removeAndReturnLastNode(head):
    node = head
    prev = None
    while node.next != None:
        prev = node
        node = node.next
    if not prev:
        # first node
        return node
    prev.next = None
    return node

def rotateOnce(head):
    node = removeAndReturnLastNode(head)
    node.next = head
    head = node
    return head

def rotate(head, k):
    n = countNodes(head)
    if n == 0 or n == 1:
        return head
    print(k % n)
    for i in range(k % n):
        head = rotateOnce(head)
    return head

def main():
    head = convertArrayToList([1,2,3,4,5])
    head = rotate(head,2)
    printList(head)

if __name__ == '__main__':
    main()
