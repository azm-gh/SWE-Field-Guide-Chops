# 3Sum (threesome)

**LeetCode:** [https://leetcode.com/problems/3sum/](https://leetcode.com/problems/3sum/)

**AlgoMaster Animation:** [https://algomaster.io/animations/dsa/3Sum](https://algomaster.io/animations/dsa/3Sum)

## Intuition

Intuition: Two-pointer after sorting. We fix one element (i) then use the
classic two-pointer technique on the remaining sorted subarray to find pairs
summing to -nums[i]. Sorting lets us skip duplicates easily and use the
two-pointer convergence pattern.

## Solutions

### `three_sum_naive` — Naive

```python
def three_sum_naive(nums: List[int]) -> List[List[int]]:
    # Time: O(n^3) — triple nested loop over all triplets
    # Space: O(n) — set stores up to n unique triplets
    n = len(nums)
    result = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(triplet)
    return [list(t) for t in result]
```

### `three_sum_optimized` — Optimized

```python
def three_sum_optimized(nums: List[int]) -> List[List[int]]:
    # Time: O(n^2) — two-pointer scan for each fixed element after O(n log n) sort
    # Space: O(1) — result excluded; sorting may use O(log n) stack
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return result
```

#### Analogy: The "Trio Team Selection" Analogy
Imagine you are a team builder organizing a group of people to form a team of exactly three members, where their collective "skill values" must sum to exactly 0 (balance out perfectly). The candidates are lined up in order from the most negative/critical to the most positive/constructive (our sorted array).

To find all unique combinations of three balanced members:

* **The Leader Selection**: You walk down the line, choosing one person at a time to be the "Anchor" of the team (`nums[i]`). Once you pick this person, your goal is to find two other members in the remaining line to perfectly balance them out (their values must sum to `-nums[i]`).
* **No Duplicates for the Leader**: If the next candidate in line has the exact same skill level as the leader you just evaluated, you skip them (`nums[i] == nums[i-1]`) because any team you form with them would just be a duplicate of what you already found.
* **The Two-Pointer Matchmakers**: For the remaining candidates, you assign two scouts:
  * **Left Scout**: Starts at the cheapest/lowest remaining skill level (`i + 1`).
  * **Right Scout**: Starts at the highest remaining skill level (`n - 1`).
* **Evaluating the Balance (total)**:
  * **Too Negative (total < 0)**: The team is overall too critical/negative. The Left Scout moves forward to find a candidate with a higher, more positive skill level (`left += 1`).
  * **Too Positive (total > 0)**: The team is overall too positive. The Right Scout moves backward to find a candidate with a lower, less positive skill level (`right -= 1`).
  * **Perfect Balance (total == 0)**: You found a perfect trio! You record the team.
* **Moving On and Avoiding Echoes**: After finding a match, both scouts step inwards (`left += 1`, `right -= 1`). If the new candidates they stand on have the same skill levels as the ones they just selected, they keep sliding past them to avoid recording duplicate teams.

