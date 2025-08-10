from typing import Optional
from collections import deque

# Public module-level state (used by callers to inspect results)
visited_order = []  # Records node visit (dequeue) order
found_path = []     # Holds the path to goal when found

def breadth_first_search(graph, start, goal):
    """
    Breadth-first search to find the shortest path from `start` to `goal`.

    - Updates `visited_order` with the order nodes are dequeued (visited).
    - When a goal is found, updates `found_path` with the shortest path.
    - Returns True if the goal is found, else False.

    Args:
        graph: Adjacency list mapping a node -> list of neighbors.
        start: Starting node.
        goal: Target node to find.

    Returns:
        bool: True if goal found, otherwise False.
    """
    # Reset the observable state for a clean run
    visited_order.clear()
    found_path.clear()

    q = deque([start])
    visited = {start}
    parent = {start: None}

    while q:
        node = q.popleft()
        visited_order.append(node)

        if node == goal:
            # Reconstruct a path by following parents
            path = []
            cur: Optional = node
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            path.reverse()

            # Mutate in place so external references see the update
            found_path.extend(path)
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                q.append(neighbor)

    return False