import heapq


def uniform_cost_search(graph, start, goal):
    """
    Uniform Cost Search on a weighted graph (non-negative edge costs).

    Args:
        graph: Adjacency list mapping a node -> list of neighbors.
        start: Starting node.
        goal: Target node to find.

    Returns:
        (total_cost, found_path) where a found_path includes start to goal
        If no found_path exists: (float('inf'), None)
    """
    # Priority p_queue of (g_cost, current_node, found_path)
    p_queue = [(0.0, start, [start])]
    best_cost = {start: 0.0}

    while p_queue:
        g_cost, node, found_path = heapq.heappop(p_queue)

        # Skip if this found_path isn't the best known
        if g_cost > best_cost.get(node, float('inf')):
            continue

        if node == goal:
            return g_cost, found_path

        for neighbor, h_cost in graph.get(node, []):
            if h_cost < 0:
                raise ValueError("Uniform Cost Search requires non-negative edge costs.")

            f_cost = g_cost + h_cost
            if f_cost < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = f_cost
                heapq.heappush(p_queue, (f_cost, neighbor, found_path + [neighbor]))

    return float('inf'), None


if __name__ == "__main__":
    # Example usage (adjacency list)
    graph1 = {
        "A": [("B", 2), ("C", 1)],
        "B": [("G", 5)],
        "C": [("B", 1), ("G", 4)],
        "G": [],
    }
    graph2 = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 2), ('E', 5)],
        'C': [('F', 3)],
        'D': [('G', 1)],
        'E': [('G', 2)],
        'F': [('G', 2)],
        'G': []
    }
    cost, path = uniform_cost_search(graph1, "A", "G")
    print(f"Optimal path: {path}\nTotal cost: {cost}")