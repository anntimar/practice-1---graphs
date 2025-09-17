# Prática 1 — Grafos

Neste repositório, implementamos os **três cenários** pedidos na prática, sempre seguindo o
pseudocódigo visto em sala e mantendo o código o mais simples possível de rodar e ler.

- **Cenário 1 (estação central)** — usamos **Floyd–Warshall** para obter a **matriz de menores caminhos**,
  somamos a linha de cada vértice e escolhemos aquele com **menor soma** (vértice central).
- **Cenário 2 (energia líquida com regeneração)** — usamos **Bellman–Ford**, pois há pesos **negativos**;
  o algoritmo também nos permite **detectar ciclo negativo** que possa contaminar o destino.
- **Cenário 3 (robô no armazém, 4 direções)** — usamos **Dijkstra** no **grid** com custos não‑negativos
  (livre = 1, difícil `~` = 3, obstáculo `#` intransponível). No final, geramos um overlay ASCII do caminho.

## Como rodar

Requer **Python 3.10+**. No terminal aberto na pasta do projeto:

```bash
# Cenário 1
python main.py cenario1 --graph graph1.txt

# Cenário 2
python main.py cenario2 --graph graph2.txt --src 0 --dst 6

# Cenário 3
python main.py cenario3 --grid grid_example.txt
```

> Obs.: em alguns ambientes pode ser `python3` no lugar de `python`.  
> As saídas aparecem no terminal **e** ficam salvas em `RESULTADO_CENARIO*.txt` e `RESULTADOS.json`.

### Exemplos de resultados (nos arquivos fornecidos)

- C1: **central = 9 (1-index)**, soma das distâncias = **219**, mais distante da central = **1** (dist **39**).
- C2: caminho **0 → 3 → 5 → 6**, custo **8.0**, **sem** ciclo negativo alcançando o destino.
- C3: custo **S→G = 26.0** e overlay ASCII do caminho com `*` no grid.

## Entradas usadas

- `graph1.txt` — grafo **não‑direcionado** com pesos (TAB como separador).
- `graph2.txt` — grafo **direcionado** com pesos (inclusive negativos).
- `grid_example.txt` — grid com `S`, `G`, `#`, `~` e células livres (`.` ou `=`). Movimento em 4 direções.

## Decisões 

- **Floyd–Warshall (C1):** precisávamos da **matriz completa** de distâncias para somar por linha; FW resolve isso direto.
- **Bellman–Ford (C2):** havia **arestas negativas** (regeneração), então Dijkstra não serve; BF também nos dá checagem de **ciclo negativo**.
- **Dijkstra em grid (C3):** todos os custos são **não‑negativos**, então Dijkstra encontra o caminho ótimo de forma eficiente.

## Estrutura do projeto

grafos_pratica1_repo/
  ├─ main.py
  ├─ src/
  │   ├─ common.py         # rotinas comuns (FW, BF, Dijkstra 1D)
  │   ├─ scenario1.py      # estação central com FW
  │   ├─ scenario2.py      # energia líquida com BF
  │   └─ scenario3.py      # Dijkstra no grid (4 vizinhos) + overlay
  ├─ graph1.txt
  ├─ graph2.txt
  ├─ grid_example.txt
  ├─ RESULTADOS.json
  ├─ RESULTADO_CENARIO1.txt
  ├─ RESULTADO_CENARIO2.txt
  └─ RESULTADO_CENARIO3.txt
```

## Observações rápidas de implementação

- Usamos `math.inf` para representar ∞ e **listas de adjacência** nos grafos.
- Em BF e Dijkstra guardamos `parent` para **reconstruir o caminho**.
- No FW tratamos múltiplas arestas mantendo o **menor peso**.
- Complexidade (bem resumida): **FW = O(n³)**; **BF = O(n·m)**; **Dijkstra ≈ O(m log n)**.

## Licença

MIT