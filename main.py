
from src.insertion_sort import insertion_sort_desc

def parse_input_list(s: str):
    # Accept comma or whitespace separated integers
    import re
    tokens = re.split(r"[\s,]+", s.strip())
    return [int(t) for t in tokens if t]

if __name__ == "__main__":
    print("Insertion Sort (Descending) Demo")
    user = input("Enter numbers (comma or space separated): ")
    arr = parse_input_list(user)
    insertion_sort_desc(arr)
    print("Sorted (descending):", arr)
