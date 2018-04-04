# Given two lists. concatenate them (that is, combine them into a single list).

# For example, given [1, 2] and [3, 4]:

# >>> concat_lists([1, 2], [3, 4])
# [1, 2, 3, 4]
# It should work if either list is empty:

# >>> concat_lists([], [1, 2])
# [1, 2]

# >>> concat_lists([1, 2], [])
# [1, 2]

# >>> concat_lists([], [])
# []


def concat_lists(list1, list2):
    """Combine lists."""

    # START SOLUTION

    for item in list2:
        list1.append(item)

    return list1