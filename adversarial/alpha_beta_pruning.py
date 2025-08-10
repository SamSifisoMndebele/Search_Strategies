from math import inf

def alphabeta(graph, node, maximizing = True, alpha=-inf, beta=inf):
    # If the node is a leaf (numeric value), return it
    if isinstance(node, (int, float)):
        return node

    if maximizing:  # MAX node
        value = -inf
        for child in graph[node]:
            value = max(value, alphabeta(graph, child, False, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # Beta cut-off
        return value
    else:  # MIN node
        value = inf
        for child in graph[node]:
            value = min(value, alphabeta(graph, child, True, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break  # Alpha cut-off
        return value