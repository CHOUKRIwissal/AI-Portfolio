"""
List Processing Functions
Advanced list operations
"""

def flatten_list(nested):
    """
    Flatten a nested list into a single-level list.
    
    Example:
        >>> flatten_list([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
    """
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def chunk_list(lst, size):
    """
    Split a list into chunks of specified size.
    
    Example:
        >>> chunk_list([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
    """
    if not lst or size <= 0:
        return []
    return [lst[i:i+size] for i in range(0, len(lst), size)]

def find_duplicates(lst):
    """
    Find all duplicate values in a list.
    
    Example:
        >>> find_duplicates([1, 2, 3, 2, 4, 5, 3])
        [2, 3]
    """
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def remove_duplicates(lst):
    """Remove duplicates from a list while preserving order"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def group_by_category(items, key_func):
    """
    Group items by a key function.
    
    Example:
        >>> group_by_category(["apple", "banana", "apricot"], len)
        {5: ["apple", "banana"], 6: ["apricot"]}
    """
    groups = {}
    for item in items:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

# Test the functions
if __name__ == "__main__":
    nested = [1, [2, 3], [4, [5, 6, [7, 8]]]]
    flat = flatten_list(nested)
    print(f"Flatten: {flat}")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chunks = chunk_list(numbers, 3)
    print(f"Chunks: {chunks}")
    
    with_dups = [1, 2, 3, 2, 4, 5, 3, 6, 7, 5]
    dups = find_duplicates(with_dups)
    print(f"Duplicates: {dups}")
    
    unique = remove_duplicates(with_dups)
    print(f"Unique: {unique}")
    
    words = ["apple", "banana", "apricot", "pear", "grape"]
    grouped = group_by_category(words, len)
    print(f"Grouped by length: {grouped}")