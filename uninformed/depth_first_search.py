# Public module-level state (used by callers to inspect results)
visited_order = []  # Records node visit order
found_path = []     # Holds the path to goal when found

def depth_first_search(graph, start, goal):
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
    # Reset the observable state for a clean run
    visited_order.clear()
    found_path.clear()

    return _backtrack(graph,  [], start,goal)


def _backtrack(graph, path, node, goal):
    # Record visit
    visited_order.append(node)
    path.append(node)

    # Goal check
    if node == goal:
        # Mutate the existing list so external references see the update
        found_path.clear()
        found_path.extend(path)
        return True  # Goal found

    # Explore neighbors safely (handle missing node with a default empty list)
    for neighbor in graph[node]:
        if _backtrack(graph, path, neighbor, goal):
            return True  # Stop once the goal is found

    path.pop()  # Backtrack
    return False