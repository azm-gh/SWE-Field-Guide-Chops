# High Level Taxonomy

A bird's-eye view of algorithmic patterns, organized by the kind of problem they solve.

---

## 1. Linear Traversals (Arrays & Strings)

Moving through linear data efficiently, optimizing O(N²) brute forces to O(N) or O(N log N).

### Two Pointers
- **Opposite Direction** — finding pairs in sorted arrays
  - *Two Sum II (LC 167), 3Sum (LC 15), Container With Most Water (LC 11)*
- **Same Direction / Fast & Slow** — detecting cycles, removing duplicates
  - *Linked List Cycle (LC 141), Move Zeroes (LC 283), Find Duplicate Number (LC 287)*

### Sliding Window
- **Fixed Window** — max sum of contiguous subarray of size K
  - *Maximum Average Subarray I (LC 643)*
- **Dynamic Window** — longest substring without repeating characters
  - *Longest Substring Without Repeating Characters (LC 3), Minimum Window Substring (LC 76)*
- **O(1) Management** — optimize window validity check from O(N) to O(1) using a `matched` counter
  - *Permutation in String (LC 567), Find All Anagrams in a String (LC 438)*

### Prefix Sum
- **Static Arrays** — range sum queries
  - *Range Sum Query (LC 303)*
- **Combined with Hashmaps** — subarray sum equals K
  - *Subarray Sum Equals K (LC 560)*

---

## 2. Core Data Structure Optimizations

Leveraging data structures to trade space for time or maintain order on the fly.

- **Hashmaps & Hash Sets** — frequency counting, duplicates, O(1) lookups
  - *Two Sum (LC 1), Group Anagrams (LC 49), Longest Consecutive Sequence (LC 128)*
- **Monotonic Stacks & Queues** — next greater/smaller element, 2D-to-1D compressions
  - **2D-to-1D Compression** — collapse grid rows into histograms, then use monotonic stack vertically
    - *Largest Rectangle in Histogram (LC 84), Maximal Rectangle (LC 85), Count Submatrices With All Ones (LC 1504)*
- **Heaps / Priority Queues** — Top K, Kth largest/smallest, merging K sorted lists
  - *Kth Largest Element (LC 215), Top K Frequent Elements (LC 347)*
- **Linked Lists** — reversals, cycle detection, merging

---

## 3. Search, Sort & Intervals

Ordering data, overlapping data, and finding targets in restricted spaces.

### Modified Binary Search
- **Search Space** — rotated sorted arrays (LC 33), search a 2D matrix (LC 74)
- **Answer Space** — Koko eating bananas (LC 875), ship packages (LC 1011)

### Intervals
- **Merging** — merge overlapping intervals (LC 56)
- **Insertions & Intersections**

### Cyclic Sort
Sorting arrays with numbers in a given range (e.g., 1 to N).

---

## 4. Relational Data (Trees, Graphs & Matrices)

Nodes and edges.

- **BFS** — level-order traversal, shortest path in unweighted graphs
  - *Word Ladder (LC 127), Number of Islands (LC 200)*
- **DFS** — pathfinding, exploring possibilities, connected components
  - *Maximum Depth of Binary Tree (LC 104), Number of Islands (LC 200)*
- **Topological Sort** — dependencies and DAGs
  - *Course Schedule (LC 207)*
- **Union Find (Disjoint Set)** — grouping, cycle detection in undirected graphs
- **Backtracking** — permutations, subsets, combinations
  - *Subsets (LC 78), N-Queens (LC 51)*

---

## 5. Dynamic Programming (State & Choice)

### 1D DP / Fibonacci Sequence
State relies on 1 or 2 previous states.
- *Climbing Stairs (LC 70), House Robber (LC 198), Min Cost Climbing Stairs (LC 746)*

### Kadane's Algorithm
Maximum subarray in one pass.
- *Maximum Subarray (LC 53), Maximum Product Subarray (LC 152)*

### Subsequence DP (LIS)
Longest Increasing Subsequence, O(N log N) with Binary Search.
- *Longest Increasing Subsequence (LC 300), Largest Divisible Subset (LC 368), Mountain Array (LC 1671)*

### Geometric Dimensions DP
Sort one dimension, run LIS on the other.
- *Russian Doll Envelopes (LC 354)*

### String DP
Longest Common Subsequence, Edit Distance, Palindromic substrings.
- *LCS (LC 1143), Edit Distance (LC 72), Palindromic Substrings (LC 647)*

### Knapsack DP
- **0/1 Knapsack** — take or leave, bounded capacity
  - *Partition Equal Subset Sum (LC 416), Target Sum (LC 494)*
- **Unbounded Knapsack** — infinite supply
  - *Coin Change (LC 322)*

### Interval DP
Collapsing or merging elements where score depends on adjacent remaining elements.
- *Burst Balloons (LC 312)*

### Matrix / 2D Grid DP
Pathfinding with obstacles, maximum square/rectangle.
- *Unique Paths (LC 62), Minimum Path Sum (LC 64), Maximal Square (LC 221)*

### Digit DP
Counting numbers in a range that fit a constraint, built digit-by-digit.
- *Number of Digit One (LC 233), Numbers At Most N Given Digit Set (LC 902)*

### Advanced DP
- **Bitmask DP** — bits to represent small state sets
- **DP on Trees** — recurrences down and up tree nodes

---

## 6. Greedy & Math

- **Greedy Algorithms** — locally optimal choice at each step
  - *Jump Game (LC 55)*
- **Math & Geometry** — prime factorization, modulo, 2D intersections
- **Bit Manipulation** — XOR tricks, bit shifting
