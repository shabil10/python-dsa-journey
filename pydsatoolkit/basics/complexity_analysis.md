# Complexity Analysis

## Introduction

This document explains the time and space complexity of the Python programs I implemented during my Data Structures and Algorithms (DSA) practice.

The purpose of this document is to understand how efficiently an algorithm uses time and memory.

It covers:

* Finding maximum and minimum elements in a list.
* Python list operations.
* Time complexity.
* Space complexity.
* Auxiliary space complexity.
* Recursion stack.

---

## 1. Maximum and Minimum Problem

### Problem

Find the maximum and minimum elements from a given list of numbers.

### Approach

I used a single loop to check every element in the list.

First, I initialized two variables, `maximum` and `minimum`, with the first element of the list.

Then I iterated through the list:

* If the current element is greater than `maximum`, I updated the maximum value.
* If the current element is smaller than `minimum`, I updated the minimum value.

Finally, I returned both values.

### Implementation

```python
def check(numbers):

    maximum = numbers[0]
    minimum = numbers[0]

    for i in numbers:

        if i > maximum:
            maximum = i

        if i < minimum:
            minimum = i

    return maximum, minimum
```

### Time Complexity

**O(n) - Linear Time**

The algorithm checks every element in the list exactly once.

If the list contains 10 elements, the loop processes 10 elements.

If the list contains 100 elements, the loop processes 100 elements.

Therefore, the execution time grows proportionally with the input size.

### Auxiliary Space Complexity

**O(1) - Constant Space**

The algorithm uses only a fixed number of additional variables:

* `maximum`
* `minimum`
* `i`

It does not create another list or any additional data structure that grows with the input size.

Therefore, the auxiliary space complexity is O(1).

---

## 2. Python List Operations

Python provides different methods to add elements to a list.

I practiced two operations:

### A. append()

The `append()` method adds an element to the end of a list.

Example:

```python
numbers = [10, 20, 30, 40]

numbers.append(50)

print(numbers)
```

Output:

```text
[10, 20, 30, 40, 50]
```

**Time Complexity: O(1) Amortized**

Python lists use dynamic arrays.

Most of the time, Python can add an element directly to the next available position.

Sometimes, the allocated memory becomes full, and Python needs to resize the list.

Resizing can take O(n) time, but it happens only occasionally.

Therefore, the amortized time complexity of append() is O(1).

### B. insert()

The `insert()` method adds an element at a specified position in a list.

Example:

```python
numbers = [10, 20, 30, 40]

numbers.insert(0, 5)

print(numbers)
```

Output:

```text
[5, 10, 20, 30, 40]
```

**Time Complexity: O(n)**

When inserting an element at index 0, Python needs to shift the existing elements one position to the right.

As the list grows, more elements need to be shifted.

Therefore, inserting an element at the beginning takes O(n) time.

### Comparison

| Operation    | Time Complexity | Reason                                        |
| ------------ | --------------- | --------------------------------------------- |
| append()     | O(1) amortized  | Adds elements at the end; occasional resizing |
| insert(0, x) | O(n)            | Existing elements need shifting               |

---

## 3. Time Complexity

Time complexity describes how the execution time of an algorithm grows when the input size increases.

It helps us understand the efficiency of an algorithm.

### A. O(1) - Constant Time

Constant time means the algorithm takes approximately the same amount of time regardless of input size.

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
```

The program accesses an element directly using its index.

Whether the list contains 5 or 5,000 elements, accessing an element by index takes O(1) time.

### B. O(n) - Linear Time

Linear time means the execution time grows proportionally with the input size.

Example:

```python
numbers = [10, 20, 30, 40, 50]

for i in numbers:
    print(i)
```

The loop processes every element in the list.

If the input contains 5 elements, the loop executes 5 times.

If the input contains 100 elements, the loop executes 100 times.

Therefore, the time complexity is O(n).

### C. O(n²) - Quadratic Time

Quadratic time occurs when the number of operations grows approximately with the square of the input size.

Example:

```python
numbers = [10, 20, 30, 40]

for i in numbers:
    for j in numbers:
        print(i, j)
```

There are two nested loops.

For every element in the outer loop, the inner loop processes all elements.

If the input contains 4 elements, the inner operation executes 16 times.

If the input contains 10 elements, it executes 100 times.

Therefore, the time complexity is O(n²).

### Time Complexity Summary

| Complexity | Name      | Example                           |
| ---------- | --------- | --------------------------------- |
| O(1)       | Constant  | Accessing a list element by index |
| O(n)       | Linear    | Traversing a list                 |
| O(n²)      | Quadratic | Nested loops                      |

---

## 4. Space Complexity

Space complexity describes how much memory an algorithm requires as the input size increases.

It includes the memory used by the algorithm during execution.

### A. Input Space

Input space is the memory occupied by the input provided to an algorithm.

Example:

```python
numbers = [10, 20, 30, 40]
```

The original list is the input provided to the algorithm.

### B. Auxiliary Space

Auxiliary space means the additional memory an algorithm uses to solve a problem, excluding the memory occupied by its input.

It helps us understand how much extra memory an algorithm requires.

### C. O(1) - Constant Auxiliary Space

An algorithm has O(1) auxiliary space when it uses a fixed amount of additional memory regardless of input size.

Example:

```python
def find_max(numbers):

    maximum = numbers[0]

    for i in numbers:

        if i > maximum:
            maximum = i

    return maximum
```

The algorithm only uses a fixed number of additional variables.

It does not create another list.

Therefore, its auxiliary space complexity is O(1).

### D. O(n) - Linear Auxiliary Space

An algorithm has O(n) auxiliary space when its additional memory grows proportionally with the input size.

Example:

```python
def copy_list(numbers):

    result = []

    for i in numbers:
        result.append(i)

    return result
```

The algorithm creates a new list and copies every element into it.

If the input contains 10 elements, the additional list contains 10 elements.

If the input contains 100 elements, the additional list contains 100 elements.

Therefore, its auxiliary space complexity is O(n).

### E. O(n²) - Quadratic Auxiliary Space

An algorithm has O(n²) auxiliary space when its additional memory grows proportionally to the square of the input size.

Example:

```python
def create_matrix(n):

    matrix = []

    for i in range(n):

        row = []

        for j in range(n):
            row.append(0)

        matrix.append(row)

    return matrix
```

The algorithm creates an n × n matrix.

If n = 3, the matrix contains 9 elements.

If n = 5, the matrix contains 25 elements.

Therefore, its auxiliary space complexity is O(n²).

### F. Recursion Stack

Recursion occurs when a function calls itself.

Each recursive function call requires memory to store information about its execution.

This information is maintained using the call stack.

Example:

```python
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)
```

If the input is 3, the function creates multiple active recursive calls.

As the input increases, the number of active calls also increases.

Therefore, the auxiliary space complexity is O(n).

---

## 5. Time Complexity vs Space Complexity

Time complexity and space complexity measure different aspects of an algorithm.

| Concept          | Meaning                                           |
| ---------------- | ------------------------------------------------- |
| Time Complexity  | How execution time grows with input size          |
| Space Complexity | How memory usage grows with input size            |
| Auxiliary Space  | How additional memory usage grows with input size |

An algorithm can have O(n) time complexity and O(1) auxiliary space complexity.

For example, traversing a list and printing every element takes O(n) time but uses O(1) auxiliary space.

---

## Conclusion

Through these exercises, I learned how to analyze the efficiency of Python algorithms.

I understood:

* How to calculate maximum and minimum values using a single loop.
* How Python list operations work.
* Why append() has O(1) amortized time complexity.
* Why insert(0, x) has O(n) time complexity.
* The differences between O(1), O(n), and O(n²).
* The differences between input space and auxiliary space.
* How recursion uses additional memory through the call stack.

Understanding time and space complexity helps me write more efficient programs and develop better problem-solving skills in Data Structures and Algorithms.
