# Comparativo — pseudocódigo x o que implementamos

A ideia aqui é mostrar, de forma bem direta, onde o nosso código bate com o que vimos em sala.
Tentamos seguir o **pseudocódigo** e só adaptar o necessário pra ficar simples de ler e rodar.

## Cenário 1 — Floyd–Warshall (matriz de menores caminhos)

**Por que usamos FW?** Neste cenário precisavamos da **distância de todo mundo para todo mundo** e também do
**somatório** das distâncias pra achar o vértice “central”. Com o Floyd–Warshall eu já tinhamos a **matriz toda**,
então ficou fácil somar a linha de cada candidato e escolher o menor.

**Pseudocódigo que vimos:**
```
inicializa dist[i][j] = +∞ e dist[i][i] = 0
para cada aresta (u,v,w): dist[u][v] = w e dist[v][u] = w
para k = 0..n-1:
  para i = 0..n-1:
    para j = 0..n-1:
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

**Onde está no código:**
- Implementação: `src/common.py` → função `floyd_warshall`
- Uso no cenário: `src/scenario1.py` → função `central_station` (somamos a linha do vértice e pego o menor)

**Observação prática:** somamos `sum(dist[central])` pra comparar candidatos. Também pegamos o mais distante
a partir do central com `max(dist[central])` (ignorando `inf`).


## Cenário 2 — Bellman–Ford (arestas com pesos negativos)

**Por que usamos BF?** Aqui a energia pode ser **negativa** (regeneração), então Dijkstra não serve. O Bellman–Ford
funciona com pesos negativos e ainda dá pra detectar **ciclo negativo** (se alcançar o destino, custo ótimo fica indefinido).

**Pseudocódigo:**
```
dist[src] = 0; demais = +∞; parent[v] = -1
repete n-1 vezes:
  para cada aresta (u,v,w):
    se dist[u] + w < dist[v]: dist[v] = dist[u] + w; parent[v] = u
// detecção de ciclo negativo (opcional, mas útil):
se existir (u,v,w) com dist[u] + w < dist[v] após as relaxações, há ciclo negativo
```

**Onde está no código:**
- Implementação: `src/common.py` → função `bellman_ford` (com marcação de vértices em ciclo negativo alcançáveis)
- Uso no cenário: `src/scenario2.py` → `min_energy_path` (reconstruimos o caminho com `parent`)

**Observação prática:** se o destino estiver “contaminado” por um ciclo negativo, marcamos e retornamos o custo `NaN`.
No `graph2.txt` isso **não** acontece; o caminho 0→3→5→6 sai com custo 8.0.


## Cenário 3 — Dijkstra no grid (4 direções, custos não‑negativos)

**Por que usamos Dijkstra?** No grid os custos são **não‑negativos** (piso normal = 1, difícil `~` = 3, obstáculo `#` é bloqueio),
então Dijkstra resolve bem. O movimento é 4‑vizinhos (N,S,L,O).

**Pseudocódigo:**
```
dist[S] = 0; demais = +∞; parent = vazio
usa fila de prioridade (dist, célula)
enquanto a fila não estiver vazia:
  pega célula u com menor dist[u]
  para cada vizinho v (4 direções):
    se custo(u→v) >= 0 e dist[u] + custo < dist[v]:
      atualiza dist[v] e parent[v] e re-insere na fila
```

**Onde está no código:**
- Implementação: `src/scenario3.py` → `dijkstra_grid` (e `overlay_path` pra desenhar `*` no trajeto)
- Regras de custo: `.` ou `=` ou `S/G` = 1; `~` = 3; `#` = intransponível

**Observação prática:** consideramos o **custo de entrar** na célula vizinha. No final, reconstruimos o caminho
com a matriz `parent` e geramos um ASCII do grid com `*`.


## Diferenças pequenas em relação ao que vimos em sala

- Usamos `math.inf` no lugar de `+∞` e listas de adjacência pra representar o grafo.
- Guardamos `parent` em BF e Dijkstra pra reconstruir o caminho (isso ajuda a mostrar o trajeto).  
- No Floyd–Warshall, tratamos múltiplas arestas mantendo o menor peso quando monto a matriz.
- Complexidade: FW = O(n³); BF = O(n·m); Dijkstra (com heap) ≈ O(m log n). Para os tamanhos dos arquivos, ficou tranquilo.


## Como testamos (com exemplos)

Dentro da pasta do projeto:
```
python main.py cenario1 --graph graph1.txt
python main.py cenario2 --graph graph2.txt --src 0 --dst 6
python main.py cenario3 --grid grid_example.txt
```

As saídas também ficam salvas em:
- `RESULTADO_CENARIO1.txt`, `RESULTADO_CENARIO2.txt`, `RESULTADO_CENARIO3.txt`
- E o consolidado: `RESULTADOS.json`

