class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def calculate():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l3 = ListNode((l1.val+l2.val) % 10)
    l3.next = ListNode((l1.val+l2.val) // 10)
    p1 = l1.next
    p2 = l2.next
    p3 = l3.next
    while True:
        if p1 and p2:
            p3.val += (p1.val + p2.val) % 10
            p3.next = ListNode((p1.val + p2.val) // 10)
            p1 = p1.next
            p2 = p2.next
            p3 = p3.next
        elif p1 and not p2:
            p3.val = (p3.val+p1.val) % 10
            p3.next = ListNode((p1.val + p3.val) // 10)
            p1 = p1.next
            p2 = p2.next
            p3 = p3.next
        elif not p1 and p2:
            p3.val = (p3.val + p2.val) % 10
            p3.next = ListNode((p2.val + p3.val) // 10)
            p1 = p1.next
            p2 = p2.next
            p3 = p3.next
        else:
            if p3.val == 0:
                p3.val= None
            break
    return l3

print(calculate().val)
print(calculate().next.val)
print(calculate().next.next.val)

