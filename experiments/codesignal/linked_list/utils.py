class Node(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def convertArrayToList(array):
    head = None
    tail = head
    for each in array:
        newNode = Node(each)
        if head == None:
            head = newNode
            tail = head
        else:
            tail.next = newNode
            tail = newNode
    return head

def printList(head):
    node = head
    while node != None:
        print(node.value)
        print
        node = node.next

def countNodes(head):
    node = head
    i = 0
    while node != None:
        i += 1
        node = node.next
    return i
