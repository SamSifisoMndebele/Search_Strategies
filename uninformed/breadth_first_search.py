from tabulate import tabulate

from graphs import graph2


def breadth_first_search(graph, goal, start = None):
    """
    Performs a breadth-first search on a graph to find a path from a start node to a goal node.

    Args:
        graph (dict): The graph to search, represented as an adjacency list.
        goal: The goal node.
        start: The start node. If not provided, the first node in the graph is used.

    Returns:
        tuple: A tuple containing the status ("SUCCESS" or "FAIL") and the path from the start to the goal node as a list. If the goal is not found, the path is None.
    """
    if not graph.keys(): return "FAIL"
    if not start: start = list(graph.keys())[0]
    
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
    if status == 'SUCCESS':
        print("Path:", " -> ".join(closed_list))
    return status, None if status == "FAIL" else closed_list


if __name__ == '__main__':
    status, _ = breadth_first_search(graph2, 'G')
    print("Result:", status)