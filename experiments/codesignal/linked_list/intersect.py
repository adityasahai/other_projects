from utils import *

def intersect(headA, headB):
    a = headA
    b = headB
    while a != b:
        a = headB if a == None else a.next
        b = headA if b == None else b.next
    return a