
# Prática 1 — Grafos

Implementações em Python para os três cenários solicitados:

- **Cenário 1 (estação central)**: Floyd–Warshall para obter todas as distâncias e somatórios.
- **Cenário 2 (energia líquida com regeneração)**: Bellman–Ford (suporta pesos negativos e detecta ciclos negativos).
- **Cenário 3 (robô no armazém)**: Dijkstra no grid (custos não-negativos; movimento 4-neigh).

## Como rodar

Requer Python 3.10+.

```bash
cd grafos_pratica1_repo
python3 main.py cenario1 --graph graph1.txt
python3 main.py cenario2 --graph graph2.txt --src 0 --dst 6
python3 main.py cenario3 --grid grid_example.txt
```

Os comandos imprimem um JSON com os resultados principais. Para o cenário 3,
o JSON inclui também um *overlay* ASCII do caminho ótimo sobre o grid.

## Estrutura

```
grafos_pratica1_repo/
  ├─ main.py
  ├─ src/
  │   ├─ common.py
  │   ├─ scenario1.py
  │   ├─ scenario2.py
  │   └─ scenario3.py
  ├─ graph1.txt
  ├─ graph2.txt
  └─ grid_example.txt
```

## Justificativa dos algoritmos

- **Cenário 1**: requer uma **matriz** de distâncias mínimas entre todos os pares
  e o **somatório** das distâncias para cada vértice (centralidade pela soma). O
  Floyd–Warshall entrega diretamente a matriz *all-pairs*, facilitando todos os itens
  de saída sem precisar rodar n vezes o Dijkstra.

- **Cenário 2**: há arestas de peso **negativo** (regeneração). É caso clássico de
  **Bellman–Ford**, que funciona para pesos negativos e detecta ciclos negativos
  (se o destino for alcançável a partir de um ciclo negativo, o custo ótimo é indefinido).

- **Cenário 3**: o grid tem custos **não-negativos** e movimento em 4 direções.
  **Dijkstra** encontra o menor custo rapidamente e é um dos algoritmos exigidos.

## Licença

MIT.
