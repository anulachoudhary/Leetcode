# Compute the sum of a list of numbers.

# For example:

# >>> sum_list([5, 3, 6, 2, 1])
# 17


def sum_list(num_list):
    """Return the sum of all numbers in list."""

    # START SOLUTION

    output = 0
    for num in num_list:
        output += num

    return output