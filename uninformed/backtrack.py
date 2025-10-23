from tabulate import tabulate

from graphs import graph1, graph2


def backtrack(graph, goal, start = None):
    """
    Perform Depth-First Search (DFS) on a graph while logging each iteration.

    This implementation is a variation of DFS that keeps track of:
    - SL (Search List): Tracks the current path from start to goal. Used for backtracking.
    - NSL (Next Search List): Queue of states to explore next. Maintains a search frontier.
    - DE (Dead Ends): States that have been fully explored and found unproductive.
    - CS (Current State): The node being processed at the current step.
    - Iteration: Each iteration is recorded and displayed in a table.

    Args:
        graph (dict): Adjacency list representation of the graph.
                      Example: {"A": ["B", "C"], "B": ["D"]}
        goal (str): The target node to search for.
        start (str): The starting node.

    Returns:
        str|list: A list representation of the path found (`[nodes...]`)
             or string "FAIL" if the goal cannot be reached.

    Example:
        >>> graph = {"A": ["B", "C"], "B": ["D"]}
        >>> result = backtrack(graph, "D", "A")
        >>> print("Result:", result)
        +--------+------+-------+--------+------+
        |   Iter | CS   | SL    | NSL    | DE   |
        +========+======+=======+========+======+
        |      0 | A    | [A]   | [A]    | []   |
        +--------+------+-------+--------+------+
        |      1 | B    | [BA]  | [BCA]  | []   |
        +--------+------+-------+--------+------+
        |      2 | D    | [DBA] | [DBCA] | []   |
        +--------+------+-------+--------+------+
        Path: A -> B -> D
        Result: ['D', 'B', 'A']
    """
    if not graph.keys(): return "FAIL"
    if not start: start = list(graph.keys())[0]

    SL = [start]
    NSL = [start]
    DE = []
    CS = start
    iteration = 0
    log = []
    
    def states(s): return "[" + "".join(s) + "]"

    while NSL:
        log.append([iteration, CS, states(SL), states(NSL), states(DE)])
        iteration += 1

        if CS == goal:
            print(tabulate(log, headers=["Iter", "CS", "SL", "NSL", "DE"], tablefmt="grid"))
            print("Path:", " -> ".join(SL[::-1]))
            return SL

        # Children of CS excluding nodes already on DE, SL, and NSL
        children = []
        for child in graph.get(CS, []):
            if child not in SL and child not in NSL and child not in DE:
                children.append(child)

        if not children:
            while SL and CS == SL[0]:
                DE.insert(0, CS)
                SL.pop(0)
                NSL.pop(0)
                if NSL: CS = NSL[0]
            if NSL: SL.insert(0, CS)
        else:
            NSL = children + NSL
            CS = NSL[0]
            SL.insert(0, CS)

    log.append([iteration, '', states(SL), states(NSL), states(DE)])
    print(tabulate(log, headers=["Iter", "CS", "SL", "NSL", "DE"], tablefmt="grid"))
    return "FAIL"


if __name__ == '__main__':
    result = backtrack(graph2, 'Q')
    print("Result:", result)
