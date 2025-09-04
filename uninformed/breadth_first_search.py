from collections import deque
from typing import Tuple

from tabulate import tabulate

from graphs import graph2


def breadth_first_search(graph, start, goal):
    """
    Perform Breadth-First Search (BFS) to find the shortest path from `start` to `goal`.

    - Returns a tuple (visited, path) if the goal is found, otherwise (None, None).
        - visited: list of visited nodes in order of visit
        - path: list of nodes to reach the goal

    Args:
        graph: Adjacency list mapping a node -> list of neighbors.
        start: Starting node.
        goal: Target node to find.

    Returns:
        Tuple:
            - visited: A list of nodes in the order they were visited.
            - path: The path from `start` to `goal` (if found), otherwise an empty list.
    """
    visited = []  # Records node visit (dequeue) order
    path = []     # Holds the path to goal when found

    q = deque([(start, [start])])  # Store (node, current_path)
    visited_set = {start}

    while q:
        node, current_path = q.popleft()
        visited.append(node)

        if node == goal:
            # Mutate in place so external references see the update
            path.extend(current_path)
            return visited, path

        for neighbor in graph[node]:
            if neighbor not in visited_set:
                visited_set.add(neighbor)
                q.append((neighbor, current_path + [neighbor]))

    return visited, None


def bfs(graph, start, goal):
    open_list = [start] # queue
    closed_list = []
    X = None
    iteration = 0
    log = []
    status = "FAIL"

    def states(s): return "[" + ",".join(s[::-1]) + "]"

    while open_list:
        log.append([iteration, X, states(open_list), states(closed_list)])
        iteration += 1
        X = open_list.pop(0)

        closed_list.append(X)

        if X == goal:
            status = "SUCCESS"
            break

        children = []
        for child in graph.get(X, []):
            if child not in open_list and child not in closed_list:
                children.append(child)

        open_list.extend(children)

    log.append([iteration + 1, X, states(open_list), states(closed_list)])
    print(tabulate(log, headers=["Iter", "X", "Open", "Closed"], tablefmt="grid"))
    print("Results:", status if status == "FAIL" else " -> ".join(closed_list))
    return status, None if status == "FAIL" else closed_list


if __name__ == '__main__':
    result = bfs(graph2, 'A', 'G')