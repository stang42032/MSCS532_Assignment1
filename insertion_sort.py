
"""Insertion Sort in monotonically decreasing order.

The algorithm iterates from left to right, inserting each element into the
already-sorted (in descending order) left subarray.
"""

from typing import List, Iterable

def insertion_sort_desc(arr: List[int]) -> List[int]:
    """Sort `arr` in-place in monotonically *decreasing* order using insertion sort.

    Returns the same list reference for convenience.
    """
    # Iterate over the list starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Shift all elements smaller than key (for descending) to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place key at its correct position
        arr[j + 1] = key

    return arr


def sorted_copy_desc(iterable: Iterable[int]) -> List[int]:
    """Return a new list that is the descending-order sorted copy of `iterable`.

    Useful when you don't want to mutate the original input.
    """
    copy = list(iterable)
    return insertion_sort_desc(copy)


if __name__ == "__main__":
    data = [7, 3, 9, -1, 9, 0, 4]
    print("Original:", data)
    insertion_sort_desc(data)
    print("Sorted (desc):", data)
