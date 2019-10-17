from treeClass import Tree

class BTree(Tree):
    empty = Tree(None)

    def __init__(self, label, left = empty, right = empty):
        for b in (left, right):
            assert isinstance(b, BTree) or b is BTree.empty
        Tree.__init__(self, label, [left, right])
    
    @property
    def root(self):
        return self.label

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def is_leaf(self):
        return [self.left, self.right] == [BTree.empty] * 2

    def __repr__(self):
        if self.is_leaf():
            return 'BTree({0})'.format(self.label)
        elif self.right is BTree.empty:
            left = repr(self.left)
            return 'BTree{0}, {1}'.format(self.label, left)
        else:
            left, right = repr(self.left), repr(self.right)
            if self.left is BTree.empty:
                left = 'BTree.empty'
            template = 'BTree({0},{1},{2})'
            return template.format(self.label, left, right)

def contents(t):
    if t is BTree.empty:
        return []
    else:
        return contents(t.left) + [t.label] + contents(t.right)

t = BTree(3, BTree(1),
             BTree(9,BTree(BTree.empty)))

