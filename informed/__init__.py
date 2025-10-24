from informed.best_first_search import best_first_search, visited_order, found_path

graph = {
    0: [4, 1, 16],
    4: [9, 13],
    13: [10, 12],
    9: [],
    10: [],
    12: [],
    1: [2, 5, 7],
    2: [],
    5: [11, 14],
    11: [],
    14: [],
    7: [],
    16: [15, 8],
    15: [],
    8: [17, 6, 3],
    17: [],
    6: [],
    3: []
}

def get_cost(costs, u, v):
    return costs.get((u, v), float('inf'))


# Heuristic: assumes nodes are integers; closer numbers are "closer" to the goal
def heuristic(n: int, goal: int) -> float:
    return abs(n - goal)

if __name__ == '__main__':
    print("Best First Search")
    if best_first_search(graph, 0, 15, heuristic):
        print("Visited order:", visited_order)
        print("Path to goal:", found_path)
    else:
        print("Goal not found")
    print()