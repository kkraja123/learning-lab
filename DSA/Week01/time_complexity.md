# Time Complexity:

- Time Complexity is about how the amount of work grows when the input grows.
- The input size increased, so the amount of work increased.

**n = the size of the input.**

## Mental Model

- Whenever you hear Time Complexity, your brain should think:
- "If the input becomes larger, how does the amount of work grow?"

**Not:**

- "How many seconds will it take?"
- This distinction is fundamental.


# Big-O:

- Big-O describes how the amount of work performed by an algorithm grows as the input size grows.
- When adding terms, Big-O keeps the dominant (fastest-growing) term.

1. Is there a loop?
2. How many times does it run?
3. What work happens inside each iteration?
4. Does that work depend on n?
5. Combine the answers.

## O(n) Linear:

- Order of n.
- If the input size becomes n, the amount of work grows roughly like n.

## Important correction

**Many beginners think:**

- O(n) means "it takes n seconds."
- It doesn't.

**It means:**

- "The number of operations grows linearly with the input size."

- When every input element is processed exactly once, the number of operations grows in proportion to the input size (n). Therefore, the time complexity is O(n).
- We ignore constants because they do not change the growth pattern of the algorithm.

## Interview Tip:

**If an interviewer asks:**

### "Why is 5n simplified to O(n)?"

**A strong answer is:**

- "Because Big-O measures the growth rate of an algorithm as the input size increases. Constant factors affect the exact runtime but not the growth pattern."


## O(n^2):

- Order of n squared
- Every one of the n items performs work on all n items.

## O(1):

- The amount of work does not depend on the input size.
- O(1) means the amount of work is independent of the input size.

**Do I already know where the data is?**
**Do I need to search for the data?**

## O(log n):

- O(log n) means each step removes a large fraction (often half) of the remaining work.
- O(log n), because each step eliminates half of the remaining input, so the amount of work grows very slowly as the input size increases.

## Mental Trigger

**When you see an algorithm that:**

- Cuts the remaining data in half,
- Divides the search space by 2,
- Discards half after each decision,

* your brain should immediately think:

**O(log n)**

- Not because it's Binary Search, but because of the halving pattern.
- The data must be sorted because the middle element tells us which half can be safely discarded.
- Split and inspect only one path (like Binary Search).

| Pattern                          | Mental Trigger  | Complexity   |
| -------------------------------- | --------------- | ------------ |
| I already know where the data is | Direct access   | **O(1)**     |
| I have to inspect one by one     | Sequential scan | **O(n)**     |
| I can discard half each step     | Halving         | **O(log n)** |

## O(n log n): 

- "Divide into halves" + "Process every element at each level"
- Split but process every element at each level (like Merge Sort).

| Rounds  | Work per Round | Total Complexity |
| ------- | -------------- | ---------------- |
| `log n` | `1`            | `O(log n)`       |
| `log n` | `n`            | `O(n log n)`     |


