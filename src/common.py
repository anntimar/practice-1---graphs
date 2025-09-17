
from typing import List, Tuple, Dict, Optional
import math
import heapq

INF = 10**15

def read_graph_undirected(path: str):
    """Reads an undirected weighted graph from a file with format:
    <num_vertices> <num_edges>
    <u> <v> <w>  (TAB or whitespace separated)  (1-indexed nodes allowed)
    Returns (n, edges) and an adjacency list (0-indexed).
    """
    with open(path, "r", encoding="utf-8") as f:
        content = [line.strip() for line in f if line.strip()]
    header = content[0].replace("\t"," ").split()
    n, m = int(header[0]), int(header[1])
    adj = [[] for _ in range(n)]
    for line in content[1:]:
        parts = line.replace("\t"," ").split()
        u, v, w = int(parts[0]), int(parts[1]), float(parts[2])
        # Convert 1-indexed to 0-indexed if needed
        if u >= 1 and (u <= n or u-1 <= n-1) and v >= 1:
            # assume 1-indexed
            u0, v0 = u-1, v-1
        else:
            u0, v0 = u, v
        adj[u0].append((v0, w))
        adj[v0].append((u0, w))
    return n, adj

def read_graph_directed(path: str):
    """Reads a directed weighted graph in the same format (possibly negative edges)."""
    with open(path, "r", encoding="utf-8") as f:
        content = [line.strip() for line in f if line.strip()]
    header = content[0].replace("\t"," ").split()
    n, m = int(header[0]), int(header[1])
    adj = [[] for _ in range(n)]
    edges = []
    for line in content[1:]:
        parts = line.replace("\t"," ").split()
        u, v, w = int(parts[0]), int(parts[1]), float(parts[2])
        adj[u].append((v, w))
        edges.append((u, v, w))
    return n, adj, edges

def floyd_warshall(n: int, adj: List[List[Tuple[int,float]]]):
    """All-pairs shortest paths for non-negative weights (and any graph without negative cycles).
    Builds dense matrix; useful when we need distances between all pairs.
    """
    dist = [[math.inf]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0.0
    for u in range(n):
        for v, w in adj[u]:
            if w < dist[u][v]:
                dist[u][v] = w
                dist[v][u] = w  # since undirected
    # Triple loop
    for k in range(n):
        dk = dist[k]
        for i in range(n):
            di = dist[i]
            ik = di[k]
            if ik == math.inf: 
                continue
            for j in range(n):
                via = ik + dk[j]
                if via < di[j]:
                    di[j] = via
    return dist

def dijkstra(n: int, adj: List[List[Tuple[int,float]]], src: int):
    dist = [math.inf]*n
    parent = [-1]*n
    dist[src] = 0.0
    pq = [(0.0, src)]
    while pq:
        d,u = heapq.heappop(pq)
        if d != dist[u]: 
            continue
        for v,w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, parent

def bellman_ford(n: int, edges: List[Tuple[int,int,float]], src: int):
    dist = [math.inf]*n
    parent = [-1]*n
    dist[src] = 0.0
    # Relax edges n-1 times
    for _ in range(n-1):
        changed = False
        for u,v,w in edges:
            if dist[u] != math.inf and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                changed = True
        if not changed:
            break
    # Detect negative cycle
    in_neg_cycle = [False]*n
    for u,v,w in edges:
        if dist[u] != math.inf and dist[u] + w < dist[v]:
            in_neg_cycle[v] = True
    # Propagate (optional)
    if any(in_neg_cycle):
        # Mark all reachable from any vertex already flagged
        from collections import deque
        q = deque([i for i,x in enumerate(in_neg_cycle) if x])
        seen = set(q)
        g = [[] for _ in range(n)]
        for u,v,w in edges:
            g[u].append(v)
        while q:
            u = q.popleft()
            for v in g[u]:
                if v not in seen:
                    seen.add(v); q.append(v)
        for v in seen:
            in_neg_cycle[v] = True
    return dist, parent, in_neg_cycle

def reconstruct_path(parent: list, target: int):
    if target == -1:
        return []
    path = []
    cur = target
    seen = set()
    while cur != -1:
        path.append(cur)
        if cur in seen:  # just in case
            break
        seen.add(cur)
        cur = parent[cur]
    path.reverse()
    return path
