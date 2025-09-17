
import argparse, json, os, sys, math
from src.scenario1 import central_station
from src.scenario2 import min_energy_path
from src.scenario3 import dijkstra_grid, overlay_path

def main():
    parser = argparse.ArgumentParser(description="Prática 1 - Grafos (3 cenários)")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("cenario1", help="Determinar estação central (grafo não-direcionado)")
    p1.add_argument("--graph", required=True, help="Caminho para graph1.txt")

    p2 = sub.add_parser("cenario2", help="Caminho mínimo com regeneração (grafo dirigido com arestas negativas)")
    p2.add_argument("--graph", required=True, help="Caminho para graph2.txt")
    p2.add_argument("--src", type=int, default=0)
    p2.add_argument("--dst", type=int, default=6)

    p3 = sub.add_parser("cenario3", help="Robô em grid com obstáculos (Dijkstra 4-direções)")
    p3.add_argument("--grid", required=True, help="Caminho para grid_example.txt")

    args = parser.parse_args()
    if args.cmd == "cenario1":
        res = central_station(args.graph)
        print(json.dumps(res, indent=2, ensure_ascii=False))
    elif args.cmd == "cenario2":
        res = min_energy_path(args.graph, args.src, args.dst)
        print(json.dumps(res, indent=2, ensure_ascii=False))
    elif args.cmd == "cenario3":
        res = dijkstra_grid(args.grid)
        overlay = overlay_path(res["grid"], res["path"])
        res_out = dict(res)
        res_out["overlay_path_ascii"] = overlay
        print(json.dumps(res_out, indent=2, ensure_ascii=False))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
