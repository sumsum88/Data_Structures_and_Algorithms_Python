class UnionFind(object):

    def __init__(self, n):
        # 親のnodeを表す
        self.par = [i for i in range(n)]

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            # 経路圧縮
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return

        self.par[x] = y


class UnionFindRank(UnionFind):

    def __init__(self, n):
        UnionFind.__init__(self, n)

        self.rank = [0 for _ in range(n)]

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.rank[x] += 1
        else:
            self.par[y] = x
            self.rank[y] += 1


class UnionFindRankCount(UnionFind):

    def __init__(self, n):
        UnionFind.__init__(self, n)

        self.rank = [0 for _ in range(n)]
        self.count = [1 for _ in range(n)]

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.count[y] += self.count[x]
        else:
            self.par[y] = x
            self.count[x] += self.count[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


if __name__ == '__main__':
    u = UnionFindRankCount(10)
    u.union(0, 1)
    u.union(0, 2)
    u.union(3, 4)
    u.union(4, 5)
    u.union(4, 6)
    u.union(5, 7)
    u.union(6, 9)
    u.union(6, 8)
    print(u.par, u.rank, u.count)
    print(u.same(0, 2))
    print(u.same(3, 2))