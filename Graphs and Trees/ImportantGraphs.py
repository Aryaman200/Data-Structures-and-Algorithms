def bfs(graph, start):
    from collections import deque
    visited = set([start])
    q = deque([start])
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return order

def dfs(graph, start, visited=None, order=None):
    if visited is None: visited = set()
    if order is None: order = []
    visited.add(start)
    order.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order

def connected_components(graph):
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            comp = dfs(graph, node)
            components.append(comp)
            visited.update(comp)
    return components

def cycle_detection_dfs(graph):
    def dfs(node, parent, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node, visited): return True
            elif neighbor != parent:
                return True
        return False
    visited = set()
    for node in graph:
        if node not in visited and dfs(node, -1, visited):
            return True
    return False

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.par[px] = py
        return True

def cycle_detection_union_find(edges, n):
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):
            return True
    return False

def topological_sort(graph):
    from collections import deque
    in_deg = {u:0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_deg[v] += 1
    q = deque([u for u in graph if in_deg[u]==0])
    res = []
    while q:
        u = q.popleft()
        res.append(u)
        for v in graph[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                q.append(v)
    return res

def dijkstra(graph, start):
    import heapq
    n = len(graph)
    heap = [(0, start)]
    dist = {start:0}
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue
        for v, cost in graph[u]:
            if v not in dist or d + cost < dist[v]:
                dist[v] = d + cost
                heapq.heappush(heap, (d+cost, v))
    return dist

def bellman_ford(edges, n, src):
    INF = float('inf')
    dist = [INF]*n
    dist[src] = 0
    for _ in range(n-1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u]+w
    # For negative cycles
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None
    return dist

def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')]*n for _ in range(n)]
    for u in range(n):
        dist[u][u] = 0
    for u in graph:
        for v, w in graph[u]:
            dist[u][v] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return dist

def kruskal(n, edges):
    uf = UnionFind(n)
    edges.sort(key=lambda x: x[2])
    mst, cost = [], 0
    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            cost += w
    return mst, cost

def prim(graph, start):
    import heapq
    visited = set()
    heap, res = [(0, start)], 0
    while heap:
        cost, u = heapq.heappop(heap)
        if u in visited: continue
        visited.add(u)
        res += cost
        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(heap, (w, v))
    return res

def graph_coloring(graph, m):
    color = {}
    def backtrack(v):
        if v == len(graph): return True
        for c in range(1, m+1):
            if all(color.get(nei, 0) != c for nei in graph[v]):
                color[v] = c
                if backtrack(v+1): return True
                color[v] = 0
        return False
    return backtrack(0)
