
from src.insertion_sort import insertion_sort_desc, sorted_copy_desc

def test_basic_descending():
    data = [5, 2, 9, 1, 5, 6]
    assert sorted_copy_desc(data) == [9, 6, 5, 5, 2, 1]

def test_already_descending():
    data = [10, 7, 3, 0, -2]
    assert sorted_copy_desc(data) == [10, 7, 3, 0, -2]

def test_with_duplicates_and_negatives():
    data = [0, -1, -1, 4, 4, 3]
    assert sorted_copy_desc(data) == [4, 4, 3, 0, -1, -1]

def test_empty_and_singleton():
    assert sorted_copy_desc([]) == []
    assert sorted_copy_desc([42]) == [42]

def test_in_place_behavior():
    data = [3, 1, 2]
    returned = insertion_sort_desc(data)
    assert returned is data
    assert data == [3, 2, 1]
