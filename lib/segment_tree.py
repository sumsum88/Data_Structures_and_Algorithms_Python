left = lambda n: 2*n + 1
right = lambda n: 2*n + 2
parent = lambda n: (n-1) // 2
inf = 1e8


class SegmentTree(object):

    def __init__(self, a):
        N = len(a)
        C = 2 ** (len(bin(N-1)) - 2)
        tree = [inf for _ in range(2 * C - 1)]

        for i in reversed(range(2 * C - 1)):
            if i >= C-1:
                tree[i] = a[i - (C - 1)]
            else:
                tree[i] = min(tree[left(i)], tree[right(i)])

        self.N = N
        self.tree = tree

    def update(self, i, v):
        N = (len(self.tree) + 1) // 2
        i = i + (N-1)
        self.tree[i] = v

        while i > 0:
            i = parent(i)
            self.tree[i] = min(self.tree[left(i)], self.tree[right(i)])
        return self.tree

    def __setitem__(self, key, value):
        self.update(key, value)

    def __repr__(self):
        return str(self.tree[self.N-1:])

    def range_min(self, i, j):
        N = (len(self.tree) + 1) // 2
        if i == j:
            return self.tree[i + (N-1)]

        def query(a, b, k=0, l=0, r=N):
            if r <= a or b <= l:
                return inf
            elif a <= l and r <= b:
                return self.tree[k]
            else:
                vl = query(a, b, left(k), l, (l+r)/2)
                vr = query(a, b, right(k), (l+r)/2, r)
                return min(vl, vr)

        return query(i, j)


if __name__ == '__main__':
    d = [2, 5, 3, 5, 1, 2, 9, 10]
    s = SegmentTree(d)
    s[5] = -3
    print(s)
    print(s.range_min(2, 5))
    print(s.range_min(1, 1))
    print(s.range_min(5, 7))