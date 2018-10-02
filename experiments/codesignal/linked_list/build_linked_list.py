from utils import printList, Node, convertArrayToList

def buildList(array, head):
    for element in array:
        newNode = Node(element)
        if head != None:
            newNode.next = head
            head = newNode
        else:
            head = newNode

    return head

def reverseList(oldList):
    newList = None
    while oldList != None:
        element = oldList
        oldList = oldList.next
        element.next = newList
        newList = element

    return newList

def reverseHeadToTail(head, tail):
    print("head", head.value)
    print("tail", tail.value)
    newList = None
    tailNext = tail.next
    oldHead = head
    i = 0
    while head != None and head != tailNext:
        element = head
        head = head.next
        if newList == None:
            element.next = tailNext
        else:
            element.next = newList
        newList = element
    printList(newList)
    print("___")
    return newList, oldHead

def findTail(head, k):
    if head == None:
        return None, False
    node = head
    i = 1
    while i < k:
        if node.next == None:
            return head, False
        node = node.next
        i += 1
    return node, True

def reverseListKAtATime(head, k):
    firstTime = True
    newHead = head
    firstHead = head
    prevTail = head
    while True:
        tail, tf = findTail(newHead, k)
        if tf != False:
            nextHead = tail.next
            newHead, newTail = reverseHeadToTail(newHead, tail)
            print("prevTail.value", prevTail.value)
            if firstTime:
                firstHead = newHead
                firstTime = False
            else:
                prevTail.next = newHead
                prevTail = newTail
            newHead = nextHead
        else:
            break
    return firstHead



def getTail(head):
    node = head
    while node.next.next != None:
        node = node.next
    print("tail", node.value)
    return node


def main():
    # head = None
    # head = buildList([1,2,3], head)
    # printList(head)
    # print("____")
    # head = buildList([23,4,5], head)
    # printList(head)
    # print("__________")
    # head = convertArrayToList([1,2,3])
    # printList(head)
    # print("reversing")
    # head = reverseList(head)
    # printList(head)
    head = convertArrayToList([1,2,3,4,5,6, 7, 8, 9, 10])
    head = reverseListKAtATime(head, 5)
    printList(head)


if __name__ == '__main__':
    main()
