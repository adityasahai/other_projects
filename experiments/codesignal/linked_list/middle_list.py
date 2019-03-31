from utils import convertArrayToList, printList, Node

def middleNode(head):
    count = 0
    n = head
    while n:
        count += 1
        n = n.next
    mid = int((count / 2) + 1)
    print("mid", mid)
    i = 1
    while(head):
        if i == mid:
            return head
        i += 1
        head = head.next

def middleNode2(head):
    tmp = head
    while tmp and tmp.next:
        head = head.next
        tmp = tmp.next.next
    return head

def main():
    head = convertArrayToList([1,2,3,4,5])
    print(middleNode2(head).value)
    head = convertArrayToList([1,2,3,4,5,6])
    print(middleNode2(head).value)
    head = convertArrayToList([1])
    print(middleNode2(head).value)

if __name__ == '__main__':
    main()