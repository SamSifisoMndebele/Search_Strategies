from typing import Optional, Tuple
from collections import deque

def breadth_first_search(graph, start, goal) -> Tuple:
    """
    Perform Breadth-First Search (BFS) to find the shortest path from `start` to `goal`.

    - Returns a tuple (visited_order, found_path) if the goal is found, otherwise (None, None).
        - visited_order: list of visited nodes in order of visit
        - found_path: list of nodes to reach the goal

    Args:
        graph: Adjacency list mapping a node -> list of neighbors.
        start: Starting node.
        goal: Target node to find.

    Returns:
        (visited_order, found_path) if found, else (None, None).
    """
    visited_order = []  # Records node visit (dequeue) order
    found_path = []     # Holds the path to goal when found

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
            return visited_order, found_path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                q.append(neighbor)

    return None, None