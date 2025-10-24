def hill_climbing(graph, goal, heuristic, start=None):
    current = start
    path = [current]

    while True:
        neighbors = graph.get(current, [])
        if not neighbors:
            break

        # Filter neighbors with valid heuristic values
        valid_neighbors = [
            n for n in neighbors if (current, n) in heuristic
        ]
        if not valid_neighbors:
            break

        # Choose neighbor with the lowest heuristic cost
        next_state = min(valid_neighbors, key=lambda n: heuristic[(current, n)])

        # Stop if no improvement
        if heuristic[(current, next_state)] >= heuristic.get((path[-2], current), float('inf')) if len(path) > 1 else float('inf'):
            break

        current = next_state
        path.append(current)

        if goal and current == goal:
            break

    return path

