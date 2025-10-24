from graphs import graph5
from graphs.heuristics import heuristic2


def hill_climbing(graph, goal, heuristic, start=None, allow_sideways=True):
    """
    Perform the hill climbing search algorithm to find a path to the goal from the start.

    This function implements the hill climbing algorithm, which is a heuristic search
    strategy. It starts at an initial node and iteratively moves to a neighbor node
    with a lower (better) heuristic value compared to the current node. The search
    stops when no neighboring state with a better (or equal, in the case of sideways
    moves if enabled) heuristic value exists, or when the goal state is reached.

    :param graph: A dictionary representing the graph, where keys are nodes and values
        are lists of neighbors.
    :param goal: The target goal node to stop the search.
    :param heuristic: A dictionary containing heuristic cost values for each node.
    :param start: Optional starting node for the search. If not provided, the first key
        from the graph is taken as the starting node.
    :param allow_sideways: A boolean flag indicating whether sideways moves (when
        heuristic values are equal) are permitted. Defaults to True.
    :return: A list representing the path from the start node to the goal or to the
        last reachable node.
    """
    if not graph.keys():  return [start]
    if not start: start = list(graph.keys())[0]

    current = start
    path = [current]

    while True:
        neighbors = graph.get(current, [])
        if not neighbors:
            break

        # Choose a neighbor with the lowest heuristic cost
        next_state = min(neighbors, key=lambda node: heuristic.get(node, float('inf')))
        current_h = heuristic.get(current, float('inf'))
        next_h = heuristic.get(next_state, float('inf'))

        # Stop if no improvement (unless sideways moves allowed)
        if next_h > current_h or (next_h == current_h and not allow_sideways):
            break

        current = next_state
        path.append(current)

        if goal and current == goal:
            break

    return path



if __name__ == '__main__':
    result = hill_climbing(graph5, '0', heuristic2)
    print("Path:", result)
