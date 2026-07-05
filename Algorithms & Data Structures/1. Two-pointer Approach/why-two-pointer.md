# Why Two-Pointer?

Use this pattern when:

- **The array is sorted** — A sorted array is the strongest signal that two-pointer might work. Pointers starting from both ends can converge toward a target in O(n).

- **Finding a pair** — The problem asks you to find two numbers satisfying a condition (e.g., adding to a target value, forming a container, etc.). Two pointers narrow down candidates in one pass.

- **In-place partitioning** — You need to rearrange elements in-place without extra memory (e.g., moving zeros to the end, separating evens/odds). One pointer tracks the "placement position" while another scans ahead.

- **Converging criteria** — The solution space shrinks monotonically: moving one pointer always makes progress toward the answer, never away from it.

### Example problems
- Move Zeroes — in-place partition
- Two Sum II — sorted pair search
- 3Sum — pair search with a fixed element
- Container With Most Water — converging width/height optimization
