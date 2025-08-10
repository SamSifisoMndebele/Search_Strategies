# Public module-level state (used by callers to inspect results)
from typing import Tuple


def depth_first_search(graph, start, goal) -> Tuple:
    """
    Depth-first backtracking search to find a path from `node` to `goal`.

    - Updates `visited_order` with the order of visited nodes.
    - When a goal is found, updates `found_path` with a copy of the path.
    - Returns True if the goal is found, else False.
    - Does not leave `path` mutated after returning.

    Args:
        graph: Adjacency list mapping a node -> list of neighbors.
        start: Starting node.
        goal: Target node to find.

    Returns:
        bool: True if goal found, otherwise False.
    """
    visited_order = []  # Records node visit order
    found_path = []  # Holds the path to goal when found

    return _backtrack(graph,  [], start,goal, visited_order, found_path)


def _backtrack(graph, path, node, goal, visited_order, found_path):
    # Record visit
    visited_order.append(node)
    path.append(node)

    # Goal check
    if node == goal:
        # Mutate the existing list so external references see the update
        found_path.clear()
        found_path.extend(path)
        return visited_order, found_path  # Goal found

    # Explore neighbors safely (handle missing node with a default empty list)
    for neighbor in graph[node]:
        if _backtrack(graph, path, neighbor, goal, visited_order, found_path) != (None, None):
            return visited_order, found_path  # Stop once the goal is found

    path.pop()  # Backtrack
    return None, None