---
title: "Python self Parameter and Instance Methods"
source: "Antigravity"
author:
published:
created: 2026-07-04
description: "A deep dive into why Python requires the self parameter, how instance method invocation works under the hood, and how to structure class state."
tags:
  - "clippings"
  - "python"
  - "oop"
---

# Python `self` Parameter & Instance Methods

In Python, `self` represents the **specific instance of a class** that is currently executing. Unlike other object-oriented languages where the instance reference is implicitly hidden (e.g., `this` in Java/C++ or JavaScript), Python requires you to explicitly declare `self` as the first parameter of any instance method.

---

## 1. The Core Concept: Why Explicit `self`?

Python’s philosophy values **"Explicit is better than implicit."** 

When you define a method inside a class, Python needs a way to know which object's data you are reading or writing. By passing `self` explicitly as the first argument, Python gives you access to the object's instance dictionary (`__dict__`).

Under the hood, when you write this:
```python
sched = Scheduler()
sched.call_soon(my_func)
```

Python automatically translates it into this class-level method call:
```python
Scheduler.call_soon(sched, my_func)
#                   ^^^^^ Python inserts the instance as the first argument!
```

---

## 2. Analysis of the `Scheduler` Example

Let's analyze this scheduler class to see how `self` functions in practice:

```python
import time
from collections import deque
import heapq

class Scheduler:
    def __init__(self):
        self.ready = deque()     # Functions ready to execute
        self.sleeping = []       # Sleeping functions (min-heap)
        self.sequence = 0 

    def call_soon(self, func):
        self.ready.append(func)

    def call_later(self, delay, func):
        self.sequence += 1
        deadline = time.time() + delay     # Expiration time
        # Priority queue
        heapq.heappush(self.sleeping, (deadline, self.sequence, func))
```

### The Role of `self` in Each Method:

*   **`__init__(self)`**: 
    *   **Purpose**: Initializes a new instance of the class.
    *   **The `self` binding**: Writing `self.ready = deque()` binds the `deque` object to that specific instance. If you wrote `ready = deque()` without `self.`, it would be a local variable that ceases to exist once `__init__` finishes running.
*   **`call_soon(self, func)`**:
    *   **Purpose**: Queue a function for immediate execution.
    *   **The `self` binding**: Accesses the unique `ready` attribute belonging to *this specific* scheduler instance (`self.ready`).
*   **`call_later(self, delay, func)`**:
    *   **Purpose**: Schedule a function to run after a delay.
    *   **The `self` binding**: Mutates the instance's state (`self.sequence`) and pushes the task onto the instance's own priority queue (`self.sleeping`).

---

## 3. Instance vs. Class vs. Static Methods

You do not always have to use `self`. The parameters of your class methods depend on their scope and decoration:

| Method Type | Decorator | First Parameter | Access Level | Common Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Instance Method** | None | `self` | Can access/modify both the **instance** state and **class** state. | Default method type for object behavior. |
| **Class Method** | `@classmethod` | `cls` | Cannot access instance state. Can access/modify **class-level** state. | Alternative constructors, factory methods. |
| **Static Method** | `@staticmethod` | *None* | Cannot access instance or class state. Acts like a regular function. | Utility functions that logically belong to the class. |

### Code Example:

```python
class Example:
    class_var = "shared"

    def __init__(self, val):
        self.val = val

    # 1. Instance Method
    def print_val(self):
        print(f"Instance val: {self.val}, Class var: {self.class_var}")

    # 2. Class Method
    @classmethod
    def modify_class_var(cls, new_val):
        cls.class_var = new_val

    # 3. Static Method
    @staticmethod
    def is_positive(num):
        return num > 0
```
