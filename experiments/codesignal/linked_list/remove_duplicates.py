from utils import printList, Node, convertArrayToList

def findDuplicatesInList(head):
    nums = set()
    duplicates = set()
    while head != None:
        if head.value in nums:
            duplicates.add(head.value)
        else:
            nums.add(head.value)
        head = head.next
    print(duplicates)

def removeDuplicates(head):
    if not head:
        return head
    fakeHead = Node(0)
    fakeHead.next = head
    pre = fakeHead
    cur = head
    while cur != None:
        while cur.next and cur.value == cur.next.value:
            cur = cur.next
        if pre.next == cur:
            pre = pre.next
        else:
            pre.next = cur.next
        cur = cur.next
    return fakeHead.next

def removeDuplicates2(head):
    if not head:
        return head
    cur = head
    while cur != None:
        n = cur
        while n.next and n.next.value == cur.value:
            n = n.next
        if cur == n:
            cur = cur.next
        else:
            cur.next = n.next
    return head



def main():
    head = convertArrayToList([1,2,3,3,4,4,5])
    head = removeDuplicates2(head)
    print("_________")
    printList(head)
    head = convertArrayToList([1,2,3,3,4])
    head = removeDuplicates2(head)
    print("_________")
    printList(head)
    head = convertArrayToList([1])
    head = removeDuplicates2(head)
    print("_________")
    printList(head)
    head = convertArrayToList([1,1,2,2])
    head = removeDuplicates2(head)
    print("_________")
    printList(head)

if __name__ == '__main__':
    main()