class Link:
    empty = ()

    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self. rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)
    
    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value

def filter_link(f, s):
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered

def extend_link(s, t):
    if empty(s):
        return t
    else:
        return Link( s.first, extend_link(s.rest, t) )

def empty(s):
    return s is Link.empty

def contains(s,v):
    if empty(s):
        return False
    elif s.first == v:
        return True
    else:
        return contains(s.rest, v)

def adjoin(s, v):
    if contains(s, v):
        return s
    else:
        return Link(v,s)

def intersect(set1, set2):
    if empty(set1) or empty(set2):
        return Link.empty
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, intersect(set1.rest, set2.rest))
        elif e1 < e2:
            return intersect(set1.rest, set2)
        elif e2 < e1:
            return intersect(set1, set2.rest)

def adjoin(s, v):
    if empty(s) or v < s.first:
        return Link(v, s)
    elif v == s.first:
        return s
    else:
        return Link(s.first, adjoin(s.rest, v))
   

def union(set1, set2):
    if empty(set1):
        return set2
    elif empty(set2):
        return set1
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, union(set1.rest, set2.rest))
        elif e1 < e2:
            return Link(e1, union(set1.rest, set2))
        elif e2 < e1:
            return Link(e2, union(set1, set2.rest))


def add(s, v):
    assert not empty(s), "Cannot add to an empty set"
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and empty(s.rest):
        s.rest = Link(v, s.rest)
    elif s.first < v:
        add(s.rest, v)
    return s

s = Link(3, Link(4, Link(5)))
