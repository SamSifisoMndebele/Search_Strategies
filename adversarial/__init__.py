from adversarial.alpha_beta_pruning import alphabeta

tree = {
    "A": ["B", "C", "D"],
    "B": [9, "F"],
    "F": [10, 12],
    "C": [2, "H", 7],
    "H": [11, 14],
    "D": [15, "K"],
    "K": [17, 6, 3],
}

if __name__ == '__main__':
    print("Alpha-Beta Pruning")
    print("Optimal value:", alphabeta(tree, 'A'))