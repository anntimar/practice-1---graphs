
# Comparativo (Pseudocódigo × Código)

Abaixo, colocamos o **pseudocódigo clássico** (forma resumida) ao lado da referência
de onde isso aparece no projeto.

## Floyd–Warshall (Cenário 1)

**Pseudocódigo (alto nível):**

1. Inicialize `dist[i][j] = +∞`; `dist[i][i] = 0`; para cada aresta `(u,v,w)`: `dist[u][v]=w`, `dist[v][u]=w` (grafo não-dirigido).
2. Para `k = 0..n-1`:
   - Para `i = 0..n-1`:
     - Para `j = 0..n-1`:
       - `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`.

**Código:** [`src/common.py:floyd_warshall`](src/common.py)

**Uso no cenário 1:** [`src/scenario1.py:central_station`](src/scenario1.py)

## Bellman–Ford (Cenário 2)

**Pseudocódigo (alto nível):**

1. `dist[src]=0`, demais `+∞`; `parent[v]=-1`.
2. Repita `n-1` vezes: para cada aresta `(u,v,w)`, se `dist[u]+w < dist[v]`, então
   atualize `dist[v]=dist[u]+w` e `parent[v]=u`.
3. Detecção de ciclo negativo: se algum `dist[u]+w < dist[v]` ainda for possível,
   então há ciclo negativo atingindo (ou propagável até) `v`.

**Código:** [`src/common.py:bellman_ford`](src/common.py)

**Uso no cenário 2:** [`src/scenario2.py:min_energy_path`](src/scenario2.py)

## Dijkstra (Cenário 3)

**Pseudocódigo (alto nível):**

1. `dist[src]=0`, demais `+∞`; `parent[v]=-1`.
2. Use uma fila de prioridade com pares `(dist, u)`.
3. Extraia `u` com menor `dist[u]`; para cada vizinho `(v,w≥0)`, se `dist[u]+w < dist[v]`
   atualize `dist[v]` e `parent[v]=u` e re-insira `(dist[v], v)`.
4. Ao final, `dist[dst]` é o custo ótimo e `parent` reconstrói o caminho.

**Código:** [`src/common.py:dijkstra`](src/common.py) e implementação 4-neigh em
[`src/scenario3.py`](src/scenario3.py).
