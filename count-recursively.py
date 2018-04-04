# >>> count_recursively([])
# 0

# >>> count_recursively([1, 2, 3])
# 3

def count_recursively(lst):
    """Return number of items in a list, using recursion."""

    # START SOLUTION

    if not lst:
        return 0

    return 1 + count_recursively(lst[1:])