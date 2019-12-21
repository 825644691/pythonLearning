class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

n = 2
def dele():
    dummy = ListNode(0)
    createNode(dummy, 1)
    s = dummy
    b = dummy
    for i in range(n+1):
        s = s.next
    while s is not None:
        s = s.next
        b = b.next

    b.next = b.next.next





def createNode(p, i):
    n = ListNode(i)
    p.next = n
    if i == 10:
        return
    createNode(p.next, i+1)




dele()