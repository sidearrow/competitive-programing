from collections import deque


class BFS:
    def __init__(self, n, graph):
        self.dq = deque()
        self.seen = [False] * n
        self.graph = graph

    def exec(self):
        self.dq.append(1)
        while 1:
            if len(self.dq) == 0:
                break
            item = self.dq.popleft()
            for v in self.graph[item]:
                if self.seen[v]:
                    continue
                self.seen[v] = True
                self.dq.append(v)