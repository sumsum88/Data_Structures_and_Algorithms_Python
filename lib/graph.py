import numpy as np
import queue


def bigraph_max_matching(xn, yn, edges_):
    """
     XとYの二部グラフの最大マッチング X={0,1,2,...|X|-1} Y={0,1,2,...,|Y|-1}
        edges[x]: xとつながるYの頂点のset
        matched[y]: yとマッチングされたXの頂点(暫定)

    :param xn: int x側のnode数
    :param yn: int y側のnode数
    :param edges_: list(tuple(int))
    :examples
        xn = 3, yn = 2
        edges = [(0, 1), (1, 0), (2, 0)]
    :return: int
    """
    edges = [set() for _ in range(xn)]
    matched = [-1] * yn

    for e in edges_:
        x, y = e
        edges[x].add(y)

    def dfs(v, visited):
        """
        :param v: X側の未マッチングの頂点の1つ
        :param visited: 空のsetを渡す（外部からの呼び出し時）
        :return: 増大路が見つかればTrue
        """
        for u in edges[v]:
            if u in visited:
                continue
            visited.add(u)
            if matched[u] == -1 or dfs(matched[u], visited):
                matched[u] = v
                return True
        return False

    return sum(dfs(s, set()) for s in range(xn))


def is_perfect_matching(G):
    """
    一般グラフの完全マッチング判定をDFSで
    :param G: 隣接行列
    :return: bool
    """
    N = len(G)
    if N == 1:
        return True

    for i in range(N):
        for j in range(i+1, N):
            if G[i, j] == 1:
                l = list(range(N))
                l.remove(i)
                l.remove(j)
                if len(l) == 0:
                    return True
                if is_perfect_matching(G[l][:, l]):
                    return True
    return False


def is_bigraph(n, edges):
    """
    二部グラフ判定

    :param n: int node数
    :param edges: list(tuple(int)) edge
        ex.) edges = [(0, 1), (1, 0), (2, 0)]
    :return: bool
    """

    color = [0 for _ in range(n)]
    graph = [set() for _ in range(n)]
    for e in edges:
        i, j = e
        graph[i].add(j)
        graph[j].add(i)

    def dfs(v, c):
        """
        :param v: node
        :param c: color (1 or -1)
        :return:
        """
        color[v] = c
        for j in graph[v]:
            if color[j] == c:
                # 隣が同じ色
                return False
            elif color[j] == 0:
                # まだ塗ってなければ塗る
                if not dfs(j, c * -1):
                    return False

        # 全ての頂点を塗れた
        return True

    # グラフが連結でない
    for i in range(n):
        if color[i] == 0:
            if not dfs(i, 1):
                return False
    return True

    # グラフが連結
    # why commented out
    # return dfs(0, 1)


def dijkstra(n, G, s, t=None):
    """
    :param n: int node数
    :param G: list(dict) グラフ
    :param s: int 開始地点
    :param t: int or None 終了地点（Noneなら全てとの距離を返す）

    :return:
        int or dict(int)
    """
    fixed = [-1 for _ in range(n)]
    q = queue.PriorityQueue()
    q.put((0, s))

    while not q.empty():
        w, x = q.get()
        if x == t:
            return w

        if fixed[x] != -1:
            # 既に訪れた
            continue

        fixed[x] = w

        for y in G[x]:
            # 全ての隣接辺に対し
            if fixed[y] == -1:
                # (dist, node)を追加
                q.put((w + G[x][y], y))

    if t is None:
        return fixed
    else:
        return None


def warshall_floyd(G, N):
    D = np.ones((N, N)) * 1e8
    for i in range(N):
        for j in range(N):
            if G[i][j]:
                D[i, j] = G[i][j]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if D[i,j] > D[i,k] + D[k,j]:
                    D[i,j] = D[i,k] + D[k,j]

    return D


def test(n=3):
    G = [{} for i in range(n)]
    n, m = map(int, input().split())
    for i in range(m):
        s, t, w = map(int, input().split())
        G[s][t] = w
        G[t][s] = w

    src, dst = map(int, input().split())
    print(dijkstra(n, G, src))


if __name__ == '__main__':
    # print(is_bigraph(4, [(0, 2), (1, 3), (0, 3)]))
    # print(is_bigraph(3, [(0, 1), (1, 2), (2, 0)]))
    test()
