import heapq
from typing import Any, Callable, Dict, Hashable, Iterable, List, Optional, Tuple

def uniform_cost_search(
    graph: Dict[Hashable, Iterable[Tuple[Hashable, float]]],
    start: Hashable,
    goal: Hashable
) -> Tuple[float, Optional[List[Hashable]]]:
    """
    Uniform Cost Search on a weighted graph (non-negative edge costs).

    Args:
        graph: dict[node] -> iterable of (a neighbor, cost)
        start: start node
        goal: goal node

    Returns:
        (total_cost, path) where a path includes start to goal
        If no path exists: (float('inf'), None)
    """
    # Priority queue of (g_cost, tie, node)
    # tie ensures a stable order for nodes with equal cost
    pq: List[Tuple[float, int, Hashable]] = []
    counter = 0
    heapq.heappush(pq, (0.0, counter, start))
    counter += 1

    best_cost: Dict[Hashable, float] = {start: 0.0}
    parent: Dict[Hashable, Optional[Hashable]] = {start: None}

    while pq:
        g, _, node = heapq.heappop(pq)

        # If this popped entry is worse than the best known, skip it
        if g != best_cost.get(node, float('inf')):
            continue

        if node == goal:
            # Reconstruct path
            path: List[Hashable] = []
            cur: Optional[Hashable] = node
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            path.reverse()
            return g, path

        for nbr, step_cost in graph.get(node, []):
            if step_cost < 0:
                raise ValueError("Uniform Cost Search requires non-negative edge costs.")
            new_cost = g + step_cost
            if new_cost < best_cost.get(nbr, float('inf')):
                best_cost[nbr] = new_cost
                parent[nbr] = node
                heapq.heappush(pq, (new_cost, counter, nbr))
                counter += 1

    return float('inf'), None


def uniform_cost_search_generic(
    start: Any,
    is_goal: Callable[[Any], bool],
    successors: Callable[[Any], Iterable[Tuple[Any, float]]],
) -> Tuple[float, Optional[List[Any]]]:
    """
    Generic Uniform Cost Search for state spaces defined by callbacks.

    Args:
        start: initial state
        is_goal(state) -> bool: goal test
        successors(state) -> iterable of (next_state, step_cost)

    Returns:
        (total_cost, path) or (inf, None) if no solution.
    """
    pq: List[Tuple[float, int, Any]] = []
    counter = 0
    heapq.heappush(pq, (0.0, counter, start))
    counter += 1

    best_cost: Dict[Any, float] = {start: 0.0}
    parent: Dict[Any, Optional[Any]] = {start: None}

    while pq:
        g, _, state = heapq.heappop(pq)

        if g != best_cost.get(state, float('inf')):
            continue

        if is_goal(state):
            path: List[Any] = []
            cur: Optional[Any] = state
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            path.reverse()
            return g, path

        for nxt, step_cost in successors(state):
            if step_cost < 0:
                raise ValueError("Uniform Cost Search requires non-negative step costs.")
            new_cost = g + step_cost
            if new_cost < best_cost.get(nxt, float('inf')):
                best_cost[nxt] = new_cost
                parent[nxt] = state
                heapq.heappush(pq, (new_cost, counter, nxt))
                counter += 1

    return float('inf'), None


if __name__ == "__main__":
    # Example usage (adjacency list)
    graph = {
        "A": [("B", 2), ("C", 1)],
        "B": [("D", 5)],
        "C": [("B", 1), ("D", 4)],
        "D": [],
    }
    cost, path = uniform_cost_search(graph, "A", "D")
    print("Cost:", cost)   # Expected optimal cost: 1 (A->C) + 1 (C->B) + 5 (B->D) = 7 vs direct A->B->D = 7, A->C->D = 5 -> Actually optimal is A->C->D = 5
    print("Path:", path)   # Expected: ['A', 'C', 'D']

    # Example usage (generic)
    start = "A"
    is_goal = lambda s: s == "D"
    successors = lambda s: iter(graph.get(s, []))
    cost2, path2 = uniform_cost_search_generic(start, is_goal, successors)
    print("Cost2:", cost2)
    print("Path2:", path2)