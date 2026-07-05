# Why Hashmaps and Hash Sets?

Use this pattern when:

- **"Have I seen this before?"** — The problem requires checking for duplicates or determining if a value already exists in the dataset. Hash sets give O(1) membership tests.

- **Counting frequencies** — You need to count how many times elements appear. A hashmap storing element → frequency is the standard tool.

- **Grouping elements** — The problem asks to group similar elements together (e.g., anagrams, same-frequency items). Use a hashmap where the key is the grouping criterion.

- **Complement lookup** — You need to find a pair that satisfies a condition (e.g., two numbers summing to a target). Store seen values and check for complements in O(1) per element.

- **Trading space for time** — Your brute-force is O(n²). A hashmap organizes data for instant lookups, reducing time to O(n) at the cost of O(n) space.

### Example problems
- Two Sum — complement lookup
- Find the Duplicate Number — membership check (Floyd's for O(1) space)
- Majority Element — frequency count
- Group Anagrams — frequency as key
- Longest Consecutive Sequence — set-based sequence detection
