# Why Modified Binary Search?

Use this pattern when:

- **The answer lives in a known range** — Instead of searching the input directly, the answer must fall within a predictable range (e.g., a speed between 1 and max(piles), a capacity between max(weight) and sum(weight)). Binary search tests each candidate in that range.

- **Sorted but rotated** — The array is sorted but shifted at an unknown pivot. Standard binary search won't work directly, but you can check which half is sorted and decide where to search.

- **Feasibility function exists** — You can write a function that, given a candidate answer, returns whether it's possible (e.g., "can we ship within D days with this capacity?"). The function is monotonic — if X works, anything larger works too.

- **Logarithmic time required** — The input size is large, and O(n) is too slow. Binary search narrows the search space exponentially.

### Example problems
- Search in Rotated Sorted Array — sorted + rotated
- Koko Eating Bananas — binary search on speed
- Search a 2D Matrix — flattened sorted matrix
- Capacity To Ship Packages — binary search on capacity
