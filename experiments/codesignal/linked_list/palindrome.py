from utils import *


def listLength(head):
    count = 0
    while head:
        head = head.next
        count += 1
    return count

def getMid(head):
    # Find middle of list
    n1 = head
    n2 = head
    while n2 and n2.next:
        n1 = n1.next
        n2 = n2.next.next
    return n1

def reverseList(head):
    newList = None
    n = head
    while n:
        nxt = n.next
        n.next = newList
        newList = n
        n = nxt
    return newList

def isPalidrome(head):
    # get middle element
    midElement = getMid(head)
    # reverse second half of the list
    if listLength(head) % 2 == 1:
        midElement = midElement.next
    newList = reverseList(midElement)
    while head and newList:
        if head.value != newList.value:
            return False
        head = head.next
        newList = newList.next
    return True

def checkReverseList():
    head = convertArrayToList([1,2,3,4,5])
    printList(reverseList(head))
    print("____")
    head = convertArrayToList([1,2,3,4,5,6,5])
    prev = head.next
    n = head.next.next
    prev.next = reverseList(n)
    printList(head)

def checkMiddle():
    head = convertArrayToList([1,2,3,4,5])
    assert(getMid(head) == 3)
    head = convertArrayToList([1,2,3,4,5,6])
    assert(getMid(head) == 4)

def checkPalindrome():
    head = convertArrayToList([1,2,3,4,4,3,2,1])
    assert(isPalidrome(head) == True)
    head = convertArrayToList([1,2,3])
    assert(isPalidrome(head) == False)
    head = convertArrayToList([1])
    assert(isPalidrome(head) == True)
    head = convertArrayToList([1,1])
    assert(isPalidrome(head) == True)
    head = convertArrayToList([1,2,3,2,1])
    assert(isPalidrome(head) == True)
    head = convertArrayToList([1,2])
    assert(isPalidrome(head) == False)

if __name__ == '__main__':
    # checkMiddle()
    # checkReverseList()
    checkPalindrome()