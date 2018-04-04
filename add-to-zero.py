# Given list of ints, return True if any two nums in list sum to 0.

# >>> add_to_zero([])
# False

# >>> add_to_zero([1])
# False

# >>> add_to_zero([1, 2, 3])
# False

# >>> add_to_zero([1, 2, 3, -2])
# True

# Given the wording of our problem, a zero in the list will always 
# make this true, since “any two numbers” could include that same zero for both numbers, and they sum to zero:

# >>> add_to_zero([0, 1, 2])
# True

def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0."""

    # START SOLUTION

    # Optimization: given that we're going to be saying "X in nums"
    # below, let's make a set of nums, so that check can happen in
    # O(1) time, rather than O(n) time.

    set_nums = set(nums)

    # It's easier and faster to look for -n in the list, rather than
    # getting each pair and adding them (and Python considers -0 == 0)

    for n in nums:
        if -n in set_nums:
            return True

    return False

    # As a more advanced note, the lovely `any()` function in Python
    # could be combined with a comprehension to write this in a very
    # pretty functional manner:

    # return any(-n in set_nums for n in nums)

    pass