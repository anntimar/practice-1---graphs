
from typing import List, Tuple
import math
from .common import read_graph_undirected, floyd_warshall

def central_station(path: str):
    n, adj = read_graph_undirected(path)
    # Como precisamos da matriz de distâncias entre todos os pares e do somatório por candidato,
    # optamos por Floyd-Warshall (um dos algoritmos da lista).
    D = floyd_warshall(n, adj)
    sums = [sum(row) for row in D]
    central = min(range(n), key=lambda i: sums[i])
    # Vetor de distâncias da estação central até os demais
    dist_vec = D[central]
    # Vértice mais distante (e valor)
    far_idx = max(range(n), key=lambda j: dist_vec[j] if dist_vec[j] < math.inf else -1)
    far_dist = dist_vec[far_idx]
    return {
        "n": n,
        "central_vertex_0idx": central,
        "central_vertex_1idx": central+1,
        "sum_distances": sums[central],
        "distances_from_central": dist_vec,
        "farthest_vertex_0idx": far_idx,
        "farthest_vertex_1idx": far_idx+1,
        "farthest_distance": far_dist,
        "distance_matrix": D,
    }
