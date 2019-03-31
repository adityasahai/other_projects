from utils import *

def detectCycle(head):
    seen = set()
    while head:
        if head in seen:
            return head
        else:
            seen.add(head)
        head = head.next
    return None

def detectCycle2(head):
    slow = head
    fast = head
    isCycle = False
    try:
        while fast and slow:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                isCycle = True
                break

    except:
        return None
    
    if isCycle:
        node = head
        while node != slow:
            node = node.next
            slow = slow.next
        return node
    else:
        return None

