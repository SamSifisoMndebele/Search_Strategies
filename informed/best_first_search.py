import heapq
from typing import List, Callable, Optional, Tuple

# Public module-level state (used by callers to inspect results)
visited_order = []  # Records node expansion order
found_path = []     # Holds the path to goal when found

def best_first_search(graph, start, goal, heuristic: Callable):
    """
    Greedy Best-First Search (GBFS).

    - Expands the node with the lowest heuristic value h(n) at each step.
    - Not guaranteed to find the shortest path, only a path guided by the heuristic.
    - Updates `visited_order` with the order nodes are expanded.
    - When the goal is found, updates `found_path` with the reconstructed path.
    - Returns True if the goal is found, else False.

    Args:
        graph: Adjacency list mapping a node -> list of neighbors.
        start: Starting node.
        goal: Target node to find.
        heuristic: Function h(n, goal) -> non-negative estimate of "distance" from n to goal.

    Returns:
        bool: True if goal found, otherwise False.
    """
    # Reset the observable state for a clean run
    visited_order.clear()
    found_path.clear()

    # Priority queue of (heuristic_value, tie_breaker, node)
    # tie_breaker prevents comparison of nodes when heuristic ties occur
    pq: List[Tuple] = []
    counter = 0
    heapq.heappush(pq, (heuristic(start, goal), counter, start))

    parent = {start: None}
    visited = set()

    while pq:
        _, _, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)

        # Record expansion order
        visited_order.append(node)

        if node == goal:
            # Reconstruct a path
            path = []
            cur: Optional = node
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            path.reverse()

            # Mutate in place so external references see the update
            found_path.extend(path)
            return True

        for neighbor in graph.get(node, []):
            if neighbor not in visited and neighbor not in parent:
                parent[neighbor] = node
                counter += 1
                heapq.heappush(pq, (heuristic(neighbor, goal), counter, neighbor))

    return False