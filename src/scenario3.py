
from typing import List, Tuple, Optional
import math, heapq

# Dijkstra no grid (4 direções, custos não-negativos).
# '.' ou '=' -> custo 1; '~' -> custo 3; '#' -> intransponível; 'S' e 'G' tratados como custo 1 no piso.

DIRS = [(-1,0),(1,0),(0,-1),(0,1)]

def parse_grid(path: str):
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    header = lines[0].split()
    R, C = int(header[0]), int(header[1])
    grid = lines[1:1+R]
    if len(grid) != R:
        raise ValueError("Grid incompleto.")
    S = G = None
    for i in range(R):
        for j,ch in enumerate(grid[i]):
            if ch == 'S':
                S = (i,j)
            elif ch == 'G':
                G = (i,j)
    if S is None or G is None:
        raise ValueError("Grid sem 'S' ou 'G'.")
    return R, C, grid, S, G

def cell_cost(ch: str) -> float:
    if ch in ('.', '=','S','G'):
        return 1.0
    if ch == '~':
        return 3.0
    if ch == '#':
        return math.inf
    # qualquer outro char vira custo 1 para robustez
    return 1.0

def dijkstra_grid(path: str):
    R, C, grid, S, G = parse_grid(path)
    dist = [[math.inf]*C for _ in range(R)]
    parent = [[None]*C for _ in range(R)]
    sr, sc = S
    gr, gc = G
    dist[sr][sc] = 0.0  # custo zero ao iniciar
    pq = [(0.0, sr, sc)]
    while pq:
        d, r, c = heapq.heappop(pq)
        if d != dist[r][c]: 
            continue
        if (r,c) == (gr,gc):
            break
        for dr,dc in DIRS:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C:
                w = cell_cost(grid[nr][nc])
                if math.isinf(w):  # obstáculo
                    continue
                nd = d + w  # custo de entrar na célula vizinha
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    parent[nr][nc] = (r,c)
                    heapq.heappush(pq, (nd, nr, nc))
    # Reconstrução do caminho
    path_cells = []
    if dist[gr][gc] != math.inf:
        cur = (gr,gc)
        while cur is not None:
            path_cells.append(cur)
            cur = parent[cur[0]][cur[1]]
        path_cells.reverse()
    return {
        "rows": R, "cols": C, "grid": grid, 
        "S": S, "G": G, "dist": dist, "path": path_cells, "cost": dist[gr][gc]
    }

def overlay_path(grid: List[str], path_cells: List[Tuple[int,int]]):
    # Devolve grid com '*' no caminho (sem sobrescrever S/G/#)
    G2 = [list(row) for row in grid]
    for (r,c) in path_cells:
        if G2[r][c] in ('S','G','#'): 
            continue
        G2[r][c] = '*'
    return "\n".join("".join(row) for row in G2)
