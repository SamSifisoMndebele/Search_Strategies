from uninformed.breadth_first_search import breadth_first_search, visited_order as bfs_visited_order, found_path as bfs_found_path
from uninformed.depth_first_search import depth_first_search, visited_order as dfs_visited_order, found_path as dfs_found_path

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

if __name__ == '__main__':
    print("Depth First Search")
    if depth_first_search(graph, 0, goal=15):
        print("Visited order:", dfs_visited_order)
        print("Path to goal:", dfs_found_path)
    else:
        print("Goal not found")
    print()

    print("Breadth First Search")
    if breadth_first_search(graph, 0, goal=15):
        print("Visited order:", bfs_visited_order)
        print("Path to goal:", bfs_found_path)
    else:
        print("Goal not found")
    print()