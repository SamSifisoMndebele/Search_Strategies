
def get_g(costs, a, b):
    return costs.get((a, b), float('inf'))


# Heuristic: assumes nodes are integers; closer numbers are "closer" to the goal
def heuristic(n: int, goal: int) -> float:
    return abs(n - goal)