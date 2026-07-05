---
title: "New notebook"
source: "https://gemini.google.com/app/a05ddf9db460434d"
author:
published:
created: 2026-06-25
description: "Gemini conversation with 20 messages"
tags:
  - "clippings"
---
**You**

how about javascript?

---


- **Empty List Initialization:** Avoid using `0`, `None`, or `[None]` when you want a clean list. Use `result_list = []` or `list()`.
- **The Mutable Default Argument Gotcha:** Never use an empty list `[]` as a function parameter default (e.g., `def func(lst=[])`), because the list is shared across every single call. Instead, use `lst=None` and initialize it inside the function.
- **In-Place (`.sort()`) vs. Out-of-Place (`sorted()`):**
	- Methods like `nums.sort()` change the data directly in memory and return `None`. Writing `nums_sorted = nums.sort()` results in `None`.
		- Global built-in functions like `sorted(nums)` leave the original data safe and return a brand-new sorted list.
- **Universal Nomenclature:** In an interview, refer to things that mutate data directly as **In-Place/Mutating Methods** ($O(1)$ space, memory-efficient but destructive), and things that return copies as **Pure/Out-of-Place Functions** (functional approach, side-effect free).
- **Language Cross-Over (JS Quirk):** Languages like C#, Java, and C++ return `void` for in-place sorting. JavaScript is the outlier—its `.sort()` mutates the data *but still returns* a reference to that mutated array, which can cause shared-reference bugs. Modern JS uses `.toSorted()` to avoid this.
- **Dictionary Manipulation:** You don't "append" to dictionaries. Use `my_dict[key] = value` or `my_dict.update()` to add pairs in-place. Use the `|` operator (Python 3.9+) to merge them out-of-place.
- **Dictionary Loops:** Use `.values()` to loop through just values, and `.items()` to unpack both `key, val` simultaneously in a `for` loop.
- **Index Errors (`IndexError: list index out of range`):** When comparing adjacent items (`i` and `i+1`), you can't loop over the values directly. You must use `range(len(lst) - 1)` so the index stops exactly one step short of the edge.
- **Subscriptable Errors (`TypeError: 'builtin_function_or_method' object is not subscriptable`):** This happens when you try to use square brackets `[]` on a function or method. It usually means you forgot the parentheses `()` when defining a list earlier (e.g., writing `sorted_nums = nums.sort` instead of `sorted()`).