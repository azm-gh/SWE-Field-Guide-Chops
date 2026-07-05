# Why Sliding Window?

Use this pattern when:

- **Contiguous elements** — The problem asks for a subset of elements that sit next to each other (subarray, substring, contiguous segment). The window naturally represents this contiguous range.

- **Fixed-size window (K elements)** — You need to find something about every group of K consecutive elements. Slide the window by removing the leftmost and adding the next element.

- **Dynamic-size window (min/max conditions)** — The prompt asks for a "minimum window," "maximum length," or "longest substring" that satisfies a condition. Expand the right pointer to grow the window, and shrink from the left when the condition is violated.

- **String/array scanning** — Problems involving substrings or subarrays with constraints on character frequency, distinct characters, or sum/maximum values.

### Key variants
- **Fixed window**: Maximum Average Subarray I
- **Variable window (unique constraint)**: Longest Substring Without Repeating Characters
- **Variable window (replacement constraint)**: Longest Repeating Character Replacement
- **Variable window (multi-condition)**: Minimum Window Substring
