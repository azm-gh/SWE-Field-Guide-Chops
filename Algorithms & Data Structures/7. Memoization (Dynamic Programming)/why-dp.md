# Why Dynamic Programming (Memoization)?

Use this pattern when:

- **Optimal substructure** — The optimal solution to the problem can be built from optimal solutions to its subproblems (e.g., the min coins for amount 10 uses the min coins for amount 9, 7, 5, etc.).

- **Overlapping subproblems** — The brute-force recursive solution computes the same subproblem multiple times. Memoization stores results to avoid recomputation.

- **"Take it or leave it" decisions** — At each step, you choose between competing options (e.g., rob this house or skip it, include this item in the knapsack or not).

- **Counting ways** — The problem asks "how many ways" to reach a goal (e.g., climb stairs, reach a grid cell, make change). Branching subproblems naturally lead to DP.

- **Minimization / maximization** — The problem asks for the minimum or maximum value possible under constraints (e.g., min coins, max profit, longest subsequence).

### How to recognize
1. Can you express the answer in terms of smaller inputs? → recurrence relation
2. Does the brute-force solution explore repeated states? → memoize
3. Can you build up from the smallest subproblem? → bottom-up DP

### Example problems
- Climbing Stairs — Fibonacci recurrence
- Coin Change — min coins, unbounded knapsack
- Longest Common Subsequence — two-sequence DP
- House Robber — linear DP with take/skip
