# Why Heap / Priority Queue?

Use this pattern when:

- **Continuous min/max access** — You need to repeatedly pull the smallest or largest element from a dynamic dataset. A heap provides O(log n) extraction and O(log n) insertion.

- **"Top K" or "Kth"** — The problem asks for the K most frequent, K largest, or K smallest elements. A min-heap of size K efficiently tracks the top K candidates in O(n log K).

- **Stream processing** — Data arrives one element at a time, and you need to answer queries about the current dataset (e.g., median of a stream, Kth largest in a stream).

- **Scheduling / merging** — Merging K sorted lists, scheduling jobs by priority, or processing tasks in order of urgency.

### Heap type cheat sheet
| Goal | Heap type | Why |
|------|-----------|-----|
| Kth largest | Min-heap of size K | Root is the smallest among the K largest |
| Kth smallest | Max-heap of size K | Root is the largest among the K smallest |
| Top K frequent | Min-heap by frequency | Evict least frequent when over size K |
| Always largest | Max-heap (negate values) | Peek/pop gives max element |
| Always smallest | Min-heap default | Peek/pop gives min element |

### Example problems
- Last Stone Weight — always smash largest, max-heap
- Kth Largest Element in an Array — min-heap of size K
- Top K Frequent Elements — frequency + min-heap of size K
