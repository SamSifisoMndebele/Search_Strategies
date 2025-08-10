from adversarial.alpha_beta_pruning import alphabeta
from informed.best_first_search import best_first_search, visited_order, found_path
from uninformed.breadth_first_search import breadth_first_search, visited_order as bfs_visited_order, found_path as bfs_found_path
from uninformed.depth_first_search import depth_first_search, visited_order as dfs_visited_order, found_path as dfs_found_path

# Graph as an adjacency list
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
    15: [],  # Goal
    8: [17, 6, 3],
    17: [],
    6: [],
    3: []
}

# Run Backtracking / DFS to find 15
print("Depth First Search")
if depth_first_search(graph, 0, goal = 15):
    print("Visited order:", dfs_visited_order)
    print("Path to goal:", dfs_found_path)
else:
    print("Goal not found")
print()

print("Breadth First Search")
if breadth_first_search(graph, 0, goal = 15):
    print("Visited order:", bfs_visited_order)
    print("Path to goal:", bfs_found_path)
else:
    print("Goal not found")
print()


# Example heuristic: assumes nodes are integers; closer numbers are "closer" to the goal
def heuristic(n: int, goal: int) -> float:
    return abs(n - goal)

print("Best First Search")
if best_first_search(graph, 0, 15, heuristic):
    print("Visited order:", visited_order)
    print("Path to goal:", found_path)
else:
    print("Goal not found")
print()

tree = {
    "A": ["B", "C", "D"],
    "B": [9, "F"],
    "F": [10, 12],
    "C": [2, "H", 7],
    "H": [11, 14],
    "D": [15, "K"],
    "K": [17, 6, 3],
}

print("Alpha-Beta Pruning")
print("Optimal value:", alphabeta(tree, 'A'))
print()
