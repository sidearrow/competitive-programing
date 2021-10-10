V_NUM = 7
E_NUM = 6
E = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
G = [[] for _ in range(V_NUM)]
for i, (a, b) in enumerate(E):
    G[a].append([b, i])
    G[b].append([a, i])


class DFS:
    def __init__(self, g, v_num, e_num):
        self.g = g
        self.seen = [False] * v_num
        self.edge = [False] * e_num

    def dfs(self, v, goal):
        if v == goal:
            return True
        for v2, e in self.g[v]:
            if not self.seen[v2]:
                self.seen[v2] = True
                res = self.dfs(v2, goal)
                if res:
                    self.edge[e] = True
                    return True
        return False


X, Y = 1, 5
dfs = DFS(G, V_NUM, E_NUM)
dfs.dfs(X, Y)

print(dfs.edge)