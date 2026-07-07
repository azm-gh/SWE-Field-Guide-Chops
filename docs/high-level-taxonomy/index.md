# High Level Taxonomy

A bird's-eye view of algorithmic patterns, organized by the kind of problem they solve.

---

## 1. Linear Traversals (Arrays & Strings)

Moving through linear data efficiently, optimizing O(N²) brute forces to O(N) or O(N log N).

### Two Pointers
- **Opposite Direction** — finding pairs in sorted arrays
- **Same Direction / Fast & Slow** — detecting cycles, removing duplicates

### Sliding Window
- **Fixed Window** — max sum of contiguous subarray of size K
- **Dynamic Window** — longest substring without repeating characters

### Prefix Sum
- **Static Arrays** — range sum queries
- **Combined with Hashmaps** — subarray sum equals K

---

## 2. Core Data Structure Optimizations

Leveraging data structures to trade space for time or maintain order on the fly.

- **Hashmaps & Hash Sets** — frequency counting, duplicates, O(1) lookups
- **Monotonic Stacks & Queues** — next greater/smaller element, 2D-to-1D compressions
- **Heaps / Priority Queues** — Top K, Kth largest/smallest, merging K sorted lists
- **Linked Lists** — reversals, cycle detection, merging

---

## 3. Search, Sort & Intervals

Ordering data, overlapping data, and finding targets in restricted spaces.

### Modified Binary Search
- **Search Space** — rotated sorted arrays
- **Answer Space** — Koko eating bananas

### Intervals
- **Merging** — merge overlapping intervals
- **Insertions & Intersections**

### Cyclic Sort
Sorting arrays with numbers in a given range (e.g., 1 to N).

---

## 4. Relational Data (Trees, Graphs & Matrices)

Nodes and edges.

- **BFS** — level-order traversal, shortest path in unweighted graphs
- **DFS** — pathfinding, exploring possibilities, connected components
- **Topological Sort** — dependencies and DAGs (course schedules)
- **Union Find (Disjoint Set)** — grouping, cycle detection in undirected graphs
- **Backtracking** — permutations, subsets, combinations (N-Queens, Sudoku)

---

## 5. Dynamic Programming (State & Choice)

### 1D DP / Fibonacci Sequence
State relies on 1 or 2 previous states (Climbing Stairs, House Robber).

### Subsequence DP (LIS)
Longest Increasing Subsequence, often optimized with Binary Search.

### String DP
Longest Common Subsequence, Edit Distance, Palindromic substrings.

### Knapsack DP
- **0/1 Knapsack** — take or leave, bounded capacity
- **Unbounded Knapsack** — infinite supply (Coin Change)

### Interval DP
Collapsing or merging elements where score depends on adjacent remaining elements (Burst Balloons).

### Matrix / 2D Grid DP
Pathfinding with obstacles, maximum square/rectangle.

### Digit DP
Counting numbers in a range that fit a constraint, built digit-by-digit.

### Advanced DP
- **Bitmask DP** — bits to represent small state sets
- **DP on Trees** — recurrences down and up tree nodes

---

## 6. Greedy & Math

- **Greedy Algorithms** — locally optimal choice at each step (Jump Game)
- **Math & Geometry** — prime factorization, modulo, 2D intersections
- **Bit Manipulation** — XOR tricks, bit shifting
