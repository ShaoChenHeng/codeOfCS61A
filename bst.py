from Btree import BTree

def balanced_bst(s):
    if not s:
        return BTree.empty
    else:
        mid = len(s) // 2
    left = balanced_bst(s[:mid])
    right = balanced_bst(s[mid+1:])
    return BTree(s[mid], left, right)


def largest(t):
    if t.right is BTree.empty:
        return t.label
    else:
        return largest(t.right)

def contains(s, v):
    if s is BTree.empty:
        return False
    elif s.root == v:
        return True
    elif s.root < v:
        return contains(s.right, v)
    elif s.root > v:
        return contains(s.left, v)

def adjoin(s,v):
    if s is BTree.empty:
        return BTree(v)
    elif s.root == v:
        return s
    elif s.root < v:
        return BTree(s.root, s.left, adjoin(s.right, v))
    elif s.root > v:
        return BTree(s.root, adjoin(s.left, v), s.right)
