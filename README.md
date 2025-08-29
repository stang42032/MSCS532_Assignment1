
# MSCS532 Assignment 1 — Insertion Sort (Descending)

This repository contains a Python implementation of the **Insertion Sort** algorithm that sorts in **monotonically decreasing** order.

## How to run

```bash
python3 main.py
```

## How to test if the insertion Sort Algorithm runs correctly with correct results

```bash
python3 -m pytest -q
```

## Files
- `insertion_sort.py` — insertion sort implementation (descending).
- `main.py` — small CLI demo using the algorithm.
- `test_insertion_sort.py` — unit tests.

## Complexity
- **Time:** O(n^2) worst/average, O(n) best (when already sorted in descending order).
- **Space:** O(1) extra (in-place).
