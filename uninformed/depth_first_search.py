from tabulate import tabulate

from graphs import graph2


def depth_first_search(graph, start, goal):
    """
    Performs a depth-first search (DFS) on a graph from a start node to a goal node.
    DFS is implemented using a stack (open_list) to explore nodes and a closed_list
    to keep track of inspected nodes. The algorithm logs each iteration's state and
    prints a tabulated representation of open and closed lists.

    :param graph: A dictionary representing the graph where the keys are node identifiers
        and the values are lists of neighboring nodes.
    :param start: The starting node of the search.
    :param goal: The target node for the search.
    :return: A tuple containing the status of the search ('SUCCESS' or 'FAIL') and the
        path to the goal if found, or None if no path exists.
    """
    open_list = [start] # stack
    closed_list = []
    X = None
    iteration = 0
    log = []
    status = "FAIL"

    def states(s): return "[" + ",".join(s) + "]"

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

        open_list = children + open_list

    log.append([iteration + 1, X, states(open_list), states(closed_list)])
    print(tabulate(log, headers=["Iter", "X", "Open", "Closed"], tablefmt="grid"))
    print("Results:", status if status == "FAIL" else " -> ".join(closed_list))
    return status, None if status == "FAIL" else closed_list


if __name__ == '__main__':
    result = depth_first_search(graph2, 'A', 'G')
