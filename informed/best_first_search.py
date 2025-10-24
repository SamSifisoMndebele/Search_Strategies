import heapq
from typing import List, Callable, Optional, Tuple
from tabulate import tabulate

from graphs import graph2
from graphs.heuristics import heuristic2

# Public module-level state (used by callers to inspect results)
visited_order = []  # Records node expansion order
found_path = []     # Holds the path to goal when found

def best_first_search(graph, goal, heuristic: Callable, start = None):
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


def bfs(graph, goal, heuristic, start):
    heuristic = lambda node: heuristic.get(node, float('inf'))
    open_l = [(start, heuristic(start))]
    closed_list = []
    came_from = {start: None}
    cost_so_far = {start: 0}
    X = None
    iteration = 0
    log = []

    while open_l:
        log.append([
            iteration, X,
            "[" + ",".join(f"{node}{h}" for node, h in open_l) + "]",
            "[" + ",".join(closed_list) + "]"
        ])
        iteration += 1
        X, _ = heapq.heappop(open_l)


        if X == goal:
            # Reconstruct path
            path = []
            while X:
                path.append(X)
                X = came_from[X]
            path.reverse()
            print(tabulate(log, headers=["Iter", "X", "Open", "Closed"], tablefmt="grid"))
            return "[" + "".join(path) + "]"

        closed_list.append(X)

        for neighbor in graph.get(X, []):
            new_cost = cost_so_far[X] + 1  # assuming uniform cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = X
                heapq.heappush(open_l, (neighbor, heuristic(neighbor)))

    log.append([iteration + 1, X, "[" + "".join(node for node, _ in open_l) + "]", "[" + "".join(closed_list) + "]"])
    print(tabulate(log, headers=["Iter", "X", "Open", "Closed"], tablefmt="grid"))
    return "FAIL"


if __name__ == '__main__':
    result = bfs(graph2, 'A', 'P', heuristic2)