# 🔍 **Uninformed Search Strategies**
These don’t use any domain-specific knowledge.

| **Strategy**                | **Key Traits**                                 | **Use Case**                        |
|-----------------------------|------------------------------------------------|-------------------------------------|
| **Breadth-First Search**    | Explores all nodes at current depth first      | Shortest path in unweighted graphs  |
| **Depth-First Search**      | Explores one branch deeply before backtracking | Memory-efficient, but may get stuck |
| **Uniform Cost Search**     | Expands node with lowest path cost             | Optimal path in weighted graphs     |
| **Depth-Limited Search**    | DFS with a depth cutoff                        | Avoids infinite paths               |
| **Iterative Deepening DFS** | Combines DFS and BFS benefits                  | Optimal and memory-efficient        |
| **Bidirectional Search**    | Searches from start and goal simultaneously    | Fast for symmetric problems         |


## 1. **Breadth-First Search (BFS)**
- Explores all nodes at the current depth before going deeper
- Uses a **queue (FIFO)** structure
- **Complete** and **optimal** for unweighted graphs
- Time & space: \(O(b^d)\), where \(b\) = branching factor, \(d\) = depth of a solution
- **Best for**: Shortest path in simple graphs

## 2. **Depth-First Search (DFS)**
- Explores one branch deeply before backtracking
- Uses a **stack (LIFO)** or recursion
- **Not guaranteed** to be complete or optimal
- Time: \(O(b^m)\), Space: \(O(m)\), where \(m\) = max depth
- **Best for**: Memory-constrained problems or when the solution is deep

## 3. **Uniform Cost Search (UCS)**
- Expands node with **the lowest cumulative path cost**
- Uses a **priority queue** based on path cost
- **Complete** and **optimal** for graphs with positive weights
- Time: Depends on cost granularity; can be exponential
- **Best for**: Weighted graphs where cost matters

## 4. **Depth-Limited Search**
- DFS with a **maximum depth cutoff**
- Avoids infinite loops in cyclic graphs
- **Incomplete** if a solution is beyond the depth limit
- **Best for**: Large or infinite search spaces

## 5. **Iterative Deepening DFS**
- Combines DFS’s low memory with BFS’s completeness
- Repeatedly runs DFS with increasing depth limits
- **Complete** and **optimal** for uniform cost
- Time: Slightly more than BFS, but space-efficient
- **Best for**: Large trees where memory is limited

## 6. **Bidirectional Search**
- Runs two simultaneous searches: from start and goal
- Stops when the two meet
- Requires the ability to reverse actions
- **Time complexity**: \(O(b^{d/2})\)
- **Best for**: Symmetric problems like pathfinding

---

# 🧠 **Informed (Heuristic) Search Strategies**
These use heuristics to guide the search.

| **Strategy**                    | **Key Traits**                                     | **Use Case**                           |
|:--------------------------------|----------------------------------------------------|----------------------------------------|
| **Greedy Best-First Search**    | Chooses node closest to goal (heuristic only)      | Fast but not always optimal            |
| **A***                          | Combines path cost + heuristic                     | Optimal if heuristic is admissible     |
| **Recursive Best-First Search** | Memory-efficient version of A*                     | Good for large search spaces           |
| **Memory-Bounded A***           | Limits memory usage (e.g., SMA*)                   | Solves large problems with constraints |
| **Hill Climbing**               | Moves to neighbor with best heuristic value        | Fast but can get stuck in local maxima |
| **Simulated Annealing**         | Allows occasional bad moves to escape local optima | Good for optimization problems         |

## 1. **Greedy Best-First Search**
- Chooses the node with **the lowest heuristic value (h(n))**
- Ignores path cost (g(n))
- **Fast**, but **not optimal or complete**
- Can get stuck in loops or dead ends
- **Best for**: Quick approximations when speed > accuracy

## 2. **A\* Search**
- Uses: \(f(n) = g(n) + h(n)\)
  - \(g(n)\): cost so far
  - \(h(n)\): estimated cost to goal
- **Complete** and **optimal** if \(h(n)\) is admissible (never overestimates)
- **Best for**: Pathfinding, planning, and optimal solutions

## 3. **Recursive Best-First Search (RBFS)**
- A memory-efficient version of A*
- Uses recursion and backtracking
- Keeps track of the best alternative paths
- **Best for**: Large search spaces with limited memory

## 4. **Memory-Bounded A\*** (e.g., SMA*)
- A* variant that limits memory usage
- Discards the least promising nodes when memory is full
- Tries to recover discarded paths if needed
- **Best for**: Real-world problems with memory constraints

## 5. **Hill Climbing**
- Always moves to a neighbor with the best heuristic value
- **Greedy** and **local** — no backtracking
- Can get stuck in:
  - **Local maxima**
  - **Plateaus**
  - **Ridges**
- **Best for**: Simple optimization problems

## 6. **Simulated Annealing**
- Inspired by metallurgy (cooling metals slowly)
- Occasionally accepts worse moves to escape local maxima
- The probability of a bad move decreases over time
- **Best for**: Complex optimization with many local optima

---

# 🎮 Adversarial Search (for Games)
- **Minimax**: Assumes opponent plays optimally
- **Alpha-Beta Pruning**: Cuts off branches that won’t affect an outcome
- **Expectimax**: Handles uncertainty (e.g., dice rolls)

---
