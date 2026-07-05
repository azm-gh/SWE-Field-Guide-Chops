# Why BFS and DFS?

Use this pattern when:

- **Keywords** — The problem mentions "trees," "graphs," "matrices," "networks," or "connected components."

- **Shortest path → BFS** — If the problem asks for the shortest path, minimum steps, or fewest transformations, BFS is the answer. BFS explores level by level, guaranteeing the first time you reach the target is the shortest distance.

- **All possibilities → DFS** — If the problem asks to explore all paths, count all ways, or determine if a path exists (without caring about shortest), DFS is natural. DFS goes deep before backtracking.

- **Connected components** — Counting islands, clusters, or connected regions in a grid or graph. Both BFS and DFS work; choose DFS for simpler recursive code or BFS for iterative stack-safe traversal.

- **Topological ordering** — Problems like course prerequisites: BFS (Kahn's algorithm) processes nodes with no incoming edges; DFS detects cycles via recursion states.

### When to choose BFS vs DFS
| BFS | DFS |
|-----|-----|
| Shortest path / minimum steps | Existence of any path |
| Level-order traversal | Counting all paths |
| Unweighted graph | Cycle detection |
| Kahn's algorithm (topological) | Backtracking problems |

### Example problems
- Maximum Depth of Binary Tree — DFS or BFS
- Number of Islands — connected components
- Course Schedule — cycle detection / topological sort
- Word Ladder — shortest path (BFS / bidirectional BFS)
