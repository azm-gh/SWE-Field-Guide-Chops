# Why Prefix Sum?

Use this pattern when:

- **Repeated range sum queries** — The problem asks multiple times for the sum of elements between different ranges (e.g., "sum between index 10 and 30"). Build a prefix array once, then answer each query in O(1).

- **Finding subarrays summing to K** — Combined with a hashmap, you can count how many contiguous subarrays sum to a target K. The key insight: `subarray(i..j) = prefix[j] - prefix[i-1]`.

- **Balance / pivot points** — The problem asks to find an index where the sum of left elements equals the sum of right elements. Prefix sums let you compute both sides in O(1) per index.

- **Cumulative comparisons** — Any problem where a running total helps answer a question about contiguous segments.

### Example problems
- Find Pivot Index — left sum vs right sum
- Subarray Sum Equals K — prefix sum + hashmap
- Range Sum Query — O(1) range queries with precomputed prefix

### Why not Monotonic Stack specifically?
Prefix sum covers the problems listed here. Monotonic stack (for next greater/smaller element patterns) is a related but distinct technique used for problems like "daily temperatures" or "largest rectangle in histogram."
