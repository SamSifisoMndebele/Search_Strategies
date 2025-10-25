from math import inf

from graphs import graph2
from graphs.heuristics import heuristics2


def alpha_beta(graph, heuristics, node, depth, maximizing = True, alpha=-inf, beta=inf):
    # Base case: depth limit or terminal node
    if depth == 0 or not graph[node]:
        return heuristics.get(node, 0)  # heuristic value

    if maximizing:  # MAX node
        max_value = -inf
        for child in graph[node]:
            value = alpha_beta(graph, heuristics, child, depth - 1, False, alpha, beta)
            max_value = max(max_value, value)
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # Beta cut-off
        return max_value
    else:  # MIN node
        min_value = inf
        for child in graph[node]:
            value = alpha_beta(graph, heuristics, child, depth - 1, True, alpha, beta)
            min_value = min(min_value, value)
            beta = min(beta, value)
            if alpha >= beta:
                break  # Alpha cut-off
        return min_value


if __name__ == '__main__':
    value = alpha_beta(graph2, heuristics2, 'A', 3)
    print("Value:", value)