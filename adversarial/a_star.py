from math import inf

import matplotlib.pyplot as plt
import networkx as nx

from graphs import graph7
from graphs.heuristics import heuristics7
from graphs.path_costs import g_costs7


def get_hierarchy_pos(graph, root, width=1., vert_gap=1.):
    """Compute hierarchical positions for nodes: top-down tree."""
    def _hierarchy_pos(G, node, left, right, depth=0, pos=None):
        if pos is None:
            pos = {}
        pos[node] = ((left + right) / 2, -depth * vert_gap)
        children = list(G.neighbors(node))
        if len(children) > 0:
            dx = (right - left) / len(children)
            for i, child in enumerate(children):
                pos = _hierarchy_pos(G, child, left + i*dx, left + (i+1)*dx, depth+1, pos)
        return pos
    return _hierarchy_pos(graph, root, 0, width)

def a_star(graph, heuristics, start, goal, g_costs, drawing=None):
    """
    A* search with edge costs and automatic tree visualization.
    Node labels: f = g + h
    """
    import heapq

    if drawing is None:
        drawing = nx.DiGraph()
        for parent, children in graph.items():
            for child in children:
                drawing.add_edge(parent, child)
        for n in drawing.nodes:
            drawing.nodes[n]["color"] = "#d3d3d3"
            drawing.nodes[n]["label"] = n

    open_set = [(heuristics[start], 0, start, [start])]  # (f, g, node, path)
    closed_set = set()

    while open_set:
        # Always pick node with smallest f
        open_set.sort(key=lambda x: x[0])
        f, g, current, path = open_set.pop(0)

        # Update node label with f = g + h
        h = heuristics.get(current, 0)
        drawing.nodes[current]["color"] = "#a1d99b"
        drawing.nodes[current]["label"] = f"{current}\nf={g}+{h}\n={g+h}"

        if current == goal:
            # Draw tree
            pos = get_hierarchy_pos(drawing, list(graph.keys())[0])
            colors = [drawing.nodes[n]["color"] for n in drawing.nodes]
            labels = {n: drawing.nodes[n]["label"] for n in drawing.nodes}

            plt.figure(figsize=(10, 6))
            nx.draw(drawing, pos, node_color=colors, with_labels=False, arrows=True, node_size=1500)
            nx.draw_networkx_labels(drawing, pos, labels, font_size=10, font_weight="bold")
            plt.title(f"A* Search Goal Reached! Path: {path}", fontsize=14)
            plt.axis("off")
            plt.show()
            return path, g

        closed_set.add(current)

        for neighbor in graph.get(current, []):
            edge_cost = g_costs.get((current, neighbor), 1)  # default cost 1 if not defined
            tentative_g = g + edge_cost
            if neighbor in closed_set:
                drawing.nodes[neighbor]["color"] = "red"
                drawing.nodes[neighbor]["label"] = f"{neighbor}\nSKIPPED"
                continue
            heapq.heappush(open_set, (tentative_g + heuristics.get(neighbor, 0), tentative_g, neighbor, path + [neighbor]))

    return None, inf


if __name__ == '__main__':
    path, cost = a_star(graph7, heuristics7, 'S', 'M', g_costs7)
    print("Path:", path)
    print("Cost:", cost)
