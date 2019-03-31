'''
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
'''

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index):
        if index+1 > self.length or self.length == 0:
            return -1
        n = self.head
        count = 0
        while index != count:
            count += 1
            n = n.next
        return n.val
    
    def addAtHead(self, val):
        node = ListNode(val)
        if self.length == 0:
            self.head = node
        else:
            node.next = self.head
            self.head = node        
        self.length += 1

    
    def addAtTail(self, val):
        node = ListNode(val)
        if self.length == 0:
            self.head = node
        else:
            n = self.head
            prev = None
            while n:
                prev = n
                n = n.next
            prev.next = node
        self.length += 1


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in 
        the linked list. If index equals to the length of 
        linked list, the node will be appended to the 
        end of linked list. If index is greater than the length, 
        the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == self.length:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        elif index < self.length:
            node = ListNode(val)
            prev = None
            n = self.head
            count = 0
            while count != index:
                prev = n
                n = n.next
                count += 1
            prev.next = node
            node.next = n
            self.length += 1

    
    def deleteAtIndex(self, index):
        if index+1 <= self.length:
            count = 0
            n = self.head
            prev = None
            while count != index:
                prev = n
                n = n.next
                count += 1
            if not prev:
                self.head = self.head.next
            else:
                prev.next = n.next
            self.length -= 1
    
    def printList(self):
        n = self.head
        while n:
            print(n.val)
            n = n.next
        print('_____')
        print("length", self.length)
        print('_____')



def checkLinkedList():
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtIndex(1,2)
    obj.printList()
    print('__')
    print(obj.get(1))
    print(obj.get(0))
    print(obj.get(2))



if __name__ == '__main__':
    checkLinkedList()