from tabulate import tabulate

from graphs import graph1


def depth_first_search(graph, start, goal):
    """
    Perform Depth-First Search (DFS) on a graph while logging each iteration.

    This implementation is a variation of DFS that keeps track of:
    - SL (Search List): The current exploration path (stack-like behavior).
    - NSL (Nodes to be Searched List): A queue of nodes to be explored next.
    - DE (Dead Ends): Nodes that were explored but found no children (backtracking).
    - CS (Current State): The node being processed at the current step.
    - Iteration logs: Each iteration is recorded and displayed in a table.

    Args:
        graph (dict): Adjacency list representation of the graph.
                      Example: {"A": ["B", "C"], "B": ["D"], "C": []}
        start (str): The starting node.
        goal (str): The target node to search for.

    Returns:
        str: A string representation of the path found (`[nodes...]`)
             or "FAIL" if the goal cannot be reached.

    Example:
        >>> graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
        >>> depth_first_search(graph, "A", "D")
        +--------+------+------+-------+------+
        | Iter   | CS   | SL   | NSL   | DE   |
        +--------+------+------+-------+------+
        | 1      | A    | [A]  | [A]   | []   |
        | 2      | B    | [BA] | [AB]  | []   |
        | 3      | D    | [DBA]| [ABD] | []   |
        +--------+------+------+-------+------+
        '[D B A]'
    """
    SL = [start]
    NSL = [start]
    DE = []
    CS = start
    iteration = 0
    log = []
    
    def states(s): return "[" + "".join(s) + "]"

    while NSL:
        iteration += 1
        log.append([iteration, CS, states(SL), states(NSL), states(DE)])

        if CS == goal:
            print(tabulate(log, headers=["Iter", "CS", "SL", "NSL", "DE"], tablefmt="grid"))
            return states(SL)

        children = [child for child in graph.get(CS, [])
                    if child not in SL and child not in NSL and child not in DE]

        if not children:
            while SL:
                DE.append(CS)
                SL.pop(0)
                NSL.pop(0)
                if NSL:
                    CS = NSL[0]
                    break
                else:
                    log.append([iteration + 1, CS, states(SL), states(NSL), states(DE)])
                    print(tabulate(log, headers=["Iter", "CS", "SL", "NSL", "DE"], tablefmt="grid"))
                    return "FAIL"
        else:
            NSL.extend(children)
            CS = children[0]
            SL.insert(0, CS)

    log.append([iteration + 1, CS, states(SL), states(NSL), states(DE)])
    print(tabulate(log, headers=["Iter", "CS", "SL", "NSL", "DE"], tablefmt="grid"))
    return "FAIL"


if __name__ == '__main__':
    result = depth_first_search(graph1, 'A', 'G')
    print("\nResult:", result)
