from math import inf

import matplotlib.pyplot as plt
import networkx as nx

from graphs.heuristics import heuristics9
from graphs.path_costs import graph9


def get_hierarchy_pos(graph, root, width=1., vert_gap=1.):
    """
    Compute hierarchical positions for nodes: top-down tree.
    """
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

def alpha_beta(graph, heuristics, node, depth, maximizing=True, alpha=-inf, beta=inf, visited=None, drawing=None):
    """
    Alpha-Beta pruning with automatic tree visualization.
    Colors:
      - Blue: explored internal nodes
      - Green: evaluated leaf nodes
      - Red: pruned nodes
    """
    # --- Initialize tree graph and visualization ---
    if drawing is None:
        drawing = nx.DiGraph()

        # Build graph structure
        for parent, children in graph.items():
            for child in children:
                drawing.add_edge(parent, child)

        # Default node styles
        for n in drawing.nodes:
            drawing.nodes[n]["color"] = "#d3d3d3"  # neutral gray
            drawing.nodes[n]["label"] = n

        # Track visited nodes
        visited = set()

        # --- Run recursive search ---
        value = alpha_beta(graph, heuristics, node, depth, maximizing, alpha, beta, visited, drawing)

        # --- After recursion, draw a tree ---
        pos = get_hierarchy_pos(drawing, list(graph.keys())[0])
        colors = [drawing.nodes[n]["color"] for n in drawing.nodes]
        labels = {n: drawing.nodes[n]["label"] for n in drawing.nodes}

        plt.figure(figsize=(10, 6))
        nx.draw(drawing, pos, node_color=colors, with_labels=False, arrows=True, node_size=1500)
        nx.draw_networkx_labels(drawing, pos, labels, font_size=10, font_weight="bold")

        plt.title(f"Alpha-Beta Pruning Result = {value}", fontsize=14)
        plt.axis("off")
        plt.show()

        return value

    # --- Recursive Alpha-Beta pruning ---
    visited.add(node)

    # Base case: depth limit or terminal node
    if depth == 0 or not graph.get(node, []):
        value = heuristics.get(node, 0)
        drawing.nodes[node]["color"] = "#a1d99b"  # green for leaf
        drawing.nodes[node]["label"] = f"{node}\n({value})"
        return value

    if maximizing:  # MAX node
        max_value = -inf
        for child in graph[node]:
            value = alpha_beta(graph, heuristics, child, depth - 1, False, alpha, beta, visited, drawing)
            max_value = max(max_value, value)
            alpha = max(alpha, value)
            if alpha >= beta:
                # --- Pruning ---
                for pruned_child in graph[node][graph[node].index(child) + 1:]:
                    if drawing.has_node(pruned_child):
                        drawing.nodes[pruned_child]["color"] = "red"
                        drawing.nodes[pruned_child]["label"] = f"{pruned_child}"
                break
        drawing.nodes[node]["color"] = "#9ecae1"  # blue for internal (max)
        drawing.nodes[node]["label"] = f"{max_value}\nɑ={alpha}\nʙ={beta}"
        return max_value

    else:   # MIN node
        min_value = inf
        for child in graph[node]:
            value = alpha_beta(graph, heuristics, child, depth - 1, True, alpha, beta, visited, drawing)
            min_value = min(min_value, value)
            beta = min(beta, value)
            if alpha >= beta:
                # --- Pruning ---
                for pruned_child in graph[node][graph[node].index(child) + 1:]:
                    if drawing.has_node(pruned_child):
                        drawing.nodes[pruned_child]["color"] = "red"
                        drawing.nodes[pruned_child]["label"] = f"{pruned_child}"
                break
        drawing.nodes[node]["color"] = "#9ecae1"  # blue for internal (min)
        drawing.nodes[node]["label"] = f"{min_value}\nɑ={alpha}\nʙ={beta}"
        return min_value


if __name__ == '__main__':
    value = alpha_beta(graph9, heuristics9, 'A', 4)
    print("Optimal Value:", value)