import os
import re
import ast

BASE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(BASE, "docs")

# Map: pattern folder name -> (doc folder, pattern number, short_pattern_folder)
PATTERNS = {
    "1. Two-pointer Approach": ("two-pointer-approach", "1"),
    "2. Sliding Window Pattern": ("sliding-window-pattern", "2"),
    "3. Modified Binary Search Pattern": ("modified-binary-search-pattern", "3"),
    "4. Hashmaps and Hash Sets": ("hashmaps-and-hash-sets", "4"),
    "5. Monotonic Stack - Prefix Sum Pattern": ("monotonic-stack-prefix-sum-pattern", "5"),
    "6. BFS and DFS": ("bfs-and-dfs", "6"),
    "7. Memoization (Dynamic Programming)": ("memoization-dynamic-programming", "7"),
    "8. Heap or Priority Queue": ("heap-priority-queue", "8"),
}

# Map: problem subfolder -> pretty title
PROBLEM_TITLES = {
    "move-zeroes": "Move Zeroes",
    "two-sum-ii-input-array-is-sorted": "Two Sum II - Input Array Is Sorted",
    "3sum": "3Sum (threesome)",
    "container-with-most-water": "Container With Most Water",
    "maximum-average-subarray-i": "Maximum Average Subarray I",
    "longest-substring-without-repeating-characters": "Longest Substring Without Repeating Characters",
    "longest-repeating-character-replacement": "Longest Repeating Character Replacement",
    "minimum-window-substring": "Minimum Window Substring",
    "search-in-rotated-sorted-array": "Search in Rotated Sorted Array",
    "koko-eating-bananas": "Koko Eating Bananas (Coco)",
    "search-a-2d-matrix": "Search a 2D Matrix",
    "capacity-to-ship-packages-within-d-days": "Capacity To Ship Packages Within D Days",
    "find-the-duplicate-number": "Find the Duplicate Number",
    "two-sum": "Two Sum",
    "majority-element": "Majority Element",
    "group-anagrams": "Group Anagrams",
    "longest-consecutive-sequence": "Longest Consecutive Sequence",
    "find-pivot-index": "Find Pivot Index",
    "subarray-sum-equals-k": "Subarray Sum Equals K",
    "range-sum-query": "Range Sum Query",
    "maximum-depth-of-binary-tree": "Maximum Depth of Binary Tree",
    "number-of-islands": "Number of Islands",
    "course-schedule": "Course Schedule",
    "word-ladder": "Word Ladder",
    "climbing-stairs": "Climbing Stairs",
    "coin-change": "Coin Change",
    "longest-common-subsequence": "Longest Common Subsequence",
    "house-robber": "House Robber",
    "last-stone-weight": "Last Stone Weight",
    "kth-largest-element-in-an-array": "Kth Largest Element in an Array",
    "top-k-frequent-elements": "Top K Frequent Elements",
}

# Map: problem subfolder -> AlgoMaster Animation URL (empty if not available)
ALGOMASTER_URLS = {
    "move-zeroes": "https://algomaster.io/animations/dsa/move-zeroes",
    "two-sum-ii-input-array-is-sorted": "https://algomaster.io/animations/dsa/two-sum-ii-input-array-is-sorted",
    "3sum": "https://algomaster.io/animations/dsa/3Sum",
    "container-with-most-water": "https://algomaster.io/animations/dsa/container-with-most-water",
    "maximum-average-subarray-i": "https://algomaster.io/animations/dsa/maximum-average-subarray-i",
    "longest-substring-without-repeating-characters": "https://algomaster.io/animations/dsa/longest-substring-without-repeating-characters",
    "longest-repeating-character-replacement": "https://algomaster.io/animations/dsa/longest-repeating-character-replacement",
    "minimum-window-substring": "https://algomaster.io/animations/dsa/minimum-window-substring",
    "search-in-rotated-sorted-array": "https://algomaster.io/animations/dsa/search-in-rotated-sorted-array",
    "koko-eating-bananas": "https://algomaster.io/animations/dsa/koko-eating-bananas",
    "search-a-2d-matrix": "https://algomaster.io/animations/dsa/search-a-2d-matrix",
    "capacity-to-ship-packages-within-d-days": "https://algomaster.io/animations/dsa/capacity-to-ship-packages-within-d-days",
    "find-the-duplicate-number": "https://algomaster.io/animations/dsa/find-the-duplicate-number",
    "two-sum": "https://algomaster.io/animations/dsa/two-sum",
    "majority-element": "https://algomaster.io/animations/dsa/majority-element",
    "group-anagrams": "https://algomaster.io/animations/dsa/group-anagrams",
    "longest-consecutive-sequence": "https://algomaster.io/animations/dsa/longest-consecutive-sequence",
    "find-pivot-index": "https://algomaster.io/animations/dsa/find-pivot-index",
    "subarray-sum-equals-k": "https://algomaster.io/animations/dsa/subarray-sum-equals-k",
    "range-sum-query": "https://algomaster.io/animations/dsa/range-sum-query-immutable",
    "number-of-islands": "https://algomaster.io/animations/dsa/number-of-islands",
    "word-ladder": "https://algomaster.io/animations/dsa/word-ladder",
    "climbing-stairs": "https://algomaster.io/animations/dsa/climbing-stairs",
    "coin-change": "https://algomaster.io/animations/dsa/coin-change",
    "longest-common-subsequence": "https://algomaster.io/animations/dsa/longest-common-subsequence",
    "house-robber": "https://algomaster.io/animations/dsa/house-robber",
    "last-stone-weight": "https://algomaster.io/animations/dsa/last-stone-weight",
    "kth-largest-element-in-an-array": "https://algomaster.io/animations/dsa/kth-largest-element-in-an-array",
    "top-k-frequent-elements": "https://algomaster.io/animations/dsa/top-k-frequent-elements",
}

# Map: problem subfolder -> LeetCode URL
LEETCODE_URLS = {
    "move-zeroes": "https://leetcode.com/problems/move-zeroes/",
    "two-sum-ii-input-array-is-sorted": "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/",
    "3sum": "https://leetcode.com/problems/3sum/",
    "container-with-most-water": "https://leetcode.com/problems/container-with-most-water/",
    "maximum-average-subarray-i": "https://leetcode.com/problems/maximum-average-subarray-i/",
    "longest-substring-without-repeating-characters": "https://leetcode.com/problems/longest-substring-without-repeating-characters/",
    "longest-repeating-character-replacement": "https://leetcode.com/problems/longest-repeating-character-replacement/",
    "minimum-window-substring": "https://leetcode.com/problems/minimum-window-substring/",
    "search-in-rotated-sorted-array": "https://leetcode.com/problems/search-in-rotated-sorted-array/",
    "koko-eating-bananas": "https://leetcode.com/problems/koko-eating-bananas/",
    "search-a-2d-matrix": "https://leetcode.com/problems/search-a-2d-matrix/",
    "capacity-to-ship-packages-within-d-days": "https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/",
    "find-the-duplicate-number": "https://leetcode.com/problems/find-the-duplicate-number/",
    "two-sum": "https://leetcode.com/problems/two-sum/",
    "majority-element": "https://leetcode.com/problems/majority-element/",
    "group-anagrams": "https://leetcode.com/problems/group-anagrams/",
    "longest-consecutive-sequence": "https://leetcode.com/problems/longest-consecutive-sequence/",
    "find-pivot-index": "https://leetcode.com/problems/find-pivot-index/",
    "subarray-sum-equals-k": "https://leetcode.com/problems/subarray-sum-equals-k/",
    "range-sum-query": "https://leetcode.com/problems/range-sum-query-immutable/",
    "maximum-depth-of-binary-tree": "https://leetcode.com/problems/maximum-depth-of-binary-tree/",
    "number-of-islands": "https://leetcode.com/problems/number-of-islands/",
    "course-schedule": "https://leetcode.com/problems/course-schedule/",
    "word-ladder": "https://leetcode.com/problems/word-ladder/",
    "climbing-stairs": "https://leetcode.com/problems/climbing-stairs/",
    "coin-change": "https://leetcode.com/problems/coin-change/",
    "longest-common-subsequence": "https://leetcode.com/problems/longest-common-subsequence/",
    "house-robber": "https://leetcode.com/problems/house-robber/",
    "last-stone-weight": "https://leetcode.com/problems/last-stone-weight/",
    "kth-largest-element-in-an-array": "https://leetcode.com/problems/kth-largest-element-in-an-array/",
    "top-k-frequent-elements": "https://leetcode.com/problems/top-k-frequent-elements/",
}


def extract_functions(filepath):
    """Extract function/class source code grouped by name."""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    # Split on top-level function/class definitions
    parts = re.split(r'^((?:def |class )\w+)', content, flags=re.MULTILINE)
    
    # Get the docstring and intuition comment
    header = ""
    lines = content.split("\n")
    in_docstring = False
    in_intuition = False
    docstring_lines = []
    intuition_lines = []
    code_start = 0
    for i, line in enumerate(lines):
        if '"""' in line:
            if not in_docstring:
                in_docstring = True
                docstring_lines.append(line)
            else:
                docstring_lines.append(line)
                in_docstring = False
                continue
        if in_docstring:
            docstring_lines.append(line)
            continue
        if line.strip().startswith("# Intuition:"):
            in_intuition = True
        if in_intuition:
            if line.strip().startswith("from ") or line.strip().startswith("import "):
                in_intuition = False
                continue
            if line.strip().startswith("def ") or line.strip().startswith("class "):
                in_intuition = False
                continue
            intuition_lines.append(line)
            continue
    return content


def extract_intuition(filepath):
    """Extract the intuition comment block."""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    match = re.search(r'^(# Intuition:.*?)(?=^from |^import |^def |^class )', content, re.MULTILINE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


def extract_analogy(filepath):
    """Extract the analogy comment block."""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    match = re.search(r'^(# #### Analogy:.*?)(?=\Z)', content, re.MULTILINE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


def extract_code_blocks(filepath):
    """Extract function/class definitions with their code."""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    
    # Remove analogy block if present so it doesn't get included in the code blocks
    content = re.sub(r'\n+# #### Analogy:.*$', '', content, flags=re.MULTILINE | re.DOTALL)
    
    # Find all top-level function/class definitions
    blocks = re.findall(r'^(?:def |class ).*?(?=^(?:def |class )|\Z)', content, re.MULTILINE | re.DOTALL)
    return [b.strip() for b in blocks]


def generate_problem_page(pattern_name, problem_folder, problem_title, leetcode_url, algomaster_url=""):
    """Generate a markdown page for a problem."""
    # Find the python file
    pattern_path = os.path.join(BASE, "Algorithms & Data Structures", pattern_name)
    py_files = [f for f in os.listdir(os.path.join(pattern_path, problem_folder)) if f.endswith(".py")]
    if not py_files:
        return None
    
    py_file = os.path.join(pattern_path, problem_folder, py_files[0])
    filepath = py_file
    
    with open(filepath, encoding="utf-8") as f:
        full_code = f.read()
    
    intuition = extract_intuition(filepath)
    analogy = extract_analogy(filepath)
    code_blocks = extract_code_blocks(filepath)
    
    # Build the markdown
    lines = [f"# {problem_title}", ""]
    lines.append(f"**LeetCode:** [{leetcode_url}]({leetcode_url})")
    if algomaster_url:
        lines.append(f"**AlgoMaster Animation:** [{algomaster_url}]({algomaster_url})")
    lines.append("")
    
    if intuition:
        lines.append("## Intuition")
        lines.append("")
        # Remove the '# ' prefix from intuition lines
        for il in intuition.split("\n"):
            lines.append(il.replace("# ", "", 1) if il.startswith("# ") else il)
        lines.append("")
    
    lines.append("## Solutions")
    lines.append("")
    
    for block in code_blocks:
        name_match = re.match(r'(def |class )(\w+)', block)
        if name_match:
            kw, name = name_match.groups()
            title = name.replace("_", " ").title()
            # Determine if naive or optimized
            if "naive" in name:
                label = "Naive"
            elif "optimized" in name:
                label = "Optimized"
            else:
                # For Range Sum Query classes
                if "Naive" in name:
                    label = "Naive"
                elif "Optimized" in name:
                    label = "Optimized"
                else:
                    label = ""
            
            if label:
                lines.append(f"### `{name}` — {label}")
            else:
                lines.append(f"### `{name}`")
            lines.append("")
            lines.append("```python")
            lines.append(block)
            lines.append("```")
            lines.append("")
            
            if (label == "Optimized" or "optimized" in name) and analogy:
                # Remove the '# ' prefix from analogy lines
                for al in analogy.split("\n"):
                    lines.append(al.replace("# ", "", 1) if al.startswith("# ") else al)
                lines.append("")
    
    return "\n".join(lines)


def main():
    # Generate overview pages and problem pages for each pattern
    for pattern_name, (doc_folder, _) in PATTERNS.items():
        pattern_path = os.path.join(BASE, "Algorithms & Data Structures", pattern_name)
        doc_path = os.path.join(DOCS, doc_folder)

        if not os.path.isdir(pattern_path):
            continue

        # Copy the why-*.md content as the overview page
        why_files = [f for f in os.listdir(pattern_path) if f.startswith("why-") and f.endswith(".md")]
        if why_files:
            src = os.path.join(pattern_path, why_files[0])
            dst = os.path.join(doc_path, "index.md")
            with open(src, encoding="utf-8") as f_in:
                content = f_in.read()
            with open(dst, "w", encoding="utf-8") as f_out:
                f_out.write(f"# {os.path.splitext(why_files[0])[0].replace('why-', '').title()}\n\n")
                f_out.write(content)
            print(f"  Created overview: {dst}")

        # Generate problem pages
        problems = [d for d in os.listdir(pattern_path) if os.path.isdir(os.path.join(pattern_path, d))]
        for prob_folder in problems:
            if prob_folder in PROBLEM_TITLES:
                title = PROBLEM_TITLES[prob_folder]
                url = LEETCODE_URLS.get(prob_folder, "")
                algo_url = ALGOMASTER_URLS.get(prob_folder, "")
                page = generate_problem_page(pattern_name, prob_folder, title, url, algo_url)
                if page:
                    doc_file = os.path.join(doc_path, f"{prob_folder}.md")
                    with open(doc_file, "w", encoding="utf-8") as f:
                        f.write(page)
                    print(f"  Created: {doc_file}")

    print("\nDone! All documentation pages generated.")


if __name__ == "__main__":
    main()
