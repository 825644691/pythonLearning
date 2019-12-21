# coding=utf-8

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))


def deep(root):
    if not root:
        return
    print(root.data)
    deep(root.left)
    deep(root.right)

# deep(tree)

def pre_travelsal(root):
    print(root.data)
    if root.left is not None:
        pre_travelsal(root.left)
    if root.right is not None:
        pre_travelsal(root.right)

pre_travelsal(tree)


def mid_travelsal(root):
    if root.left is not None:
        mid_travelsal(root.left)
    print(root.data)
    if root.right is not None:
        mid_travelsal(root.right)


def post_travelsal(root):
    if root.left is not None:
        post_travelsal(root.left)
    if root.right is not None:
        post_travelsal(root.right)
    print(root.data)


def maxdepth(root):
    if not root:
        return 0
    return max(maxdepth(root.left), maxdepth(root.right)) + 1


print(maxdepth(tree))


def isSameTree(p, q):
    if not p and not q:
        return True
    elif p and q:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))

def link_reverse(linkedlist):
    cur = linkedlist.next
    pre = linkedlist
    pre.next = None
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre






# 合并两个有序列表

l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]
l3 = []

def _recursion_merge_list():
    if not l1 or not l2:
        l3.extend(l1)
        l3.extend(l2)
        return
    if l1[0] < l2[0]:
        l3.append(l1[0])
        del l1[0]
    else:
        l3.append(l2[0])
        del l2[0]
    return _recursion_merge_list()


_recursion_merge_list()
print(l3)
