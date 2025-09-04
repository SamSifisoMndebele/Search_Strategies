from tabulate import tabulate

from graphs import graph2


def depth_first_search(graph, start, goal):
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
