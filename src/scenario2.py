
from typing import List, Tuple
from .common import read_graph_directed, bellman_ford, reconstruct_path

def min_energy_path(path: str, src: int = 0, dst: int = 6):
    n, adj, edges = read_graph_directed(path)
    dist, parent, in_neg_cycle = bellman_ford(n, edges, src)
    if any(in_neg_cycle):
        # Se destino faz parte (ou é alcançável de) um ciclo negativo, o custo é indefinido
        return {
            "has_negative_cycle_reaching_dst": in_neg_cycle[dst],
            "distances": dist,
            "parent": parent,
            "path": [],
            "cost": float("nan"),
        }
    path_nodes = reconstruct_path(parent, dst)
    cost = dist[dst]
    return {
        "has_negative_cycle_reaching_dst": False,
        "distances": dist,
        "parent": parent,
        "path": path_nodes,
        "cost": cost,
    }
