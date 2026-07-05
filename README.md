# SWE Field Guide Chops

Software engineering solutions organized by algorithmic pattern — each with a **naive** and an **optimized** solution.

## Patterns

| # | Pattern | Problems |
|---|---------|----------|
| 1 | Two-pointer Approach | Move Zeroes, Two Sum II, 3Sum, Container With Most Water |
| 2 | Sliding Window Pattern | Maximum Avg Subarray, Longest Substring, Char Replacement, Min Window Substring |
| 3 | Modified Binary Search | Rotated Sorted Array, Koko Bananas, 2D Matrix, Ship Packages |
| 4 | Hashmaps and Hash Sets | Duplicate Number, Two Sum, Majority Element, Group Anagrams, Longest Consecutive |
| 5 | Prefix Sum Pattern | Pivot Index, Subarray Sum K, Range Sum Query |
| 6 | BFS and DFS | Max Depth, Islands, Course Schedule, Word Ladder |
| 7 | Dynamic Programming | Climbing Stairs, Coin Change, LCS, House Robber |
| 8 | Heap / Priority Queue | Last Stone Weight, Kth Largest, Top K Frequent |

## Structure

```
Algorithms & Data Structures/
├── 1. Two-pointer Approach/
│   ├── why-this-pattern.md      # Intuition guide
│   └── problem-name/
│       └── problem_name.py      # Naive + optimized solutions
├── 2. Sliding Window Pattern/
├── ...
└── DS and Algorithms Quest/

System Design/
└── High domain overview/
```

## Site

Published with MkDocs + Material theme:  
https://azm-gh.github.io/SWE-Field-Guide-Chops/

### Deploy locally

```powershell
python -m mkdocs serve    # dev server at http://127.0.0.1:8000
python -m mkdocs gh-deploy --clean   # publish to GitHub Pages
```
