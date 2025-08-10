from uninformed.breadth_first_search import breadth_first_search
from uninformed.depth_first_search import depth_first_search

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
    visited_order, found_path = depth_first_search(graph, 0, goal=15)
    if visited_order is not None and found_path is not None:
        print("Visited order:", visited_order)
        print("Path to goal:", found_path)
    else:
        print("Goal not found")
    print()

    print("Breadth First Search")
    visited_order, found_path = breadth_first_search(graph, 0, goal=15)
    if visited_order is not None and found_path is not None:
        print("Visited order:", visited_order)
        print("Path to goal:", found_path)
    else:
        print("Goal not found")
    print()