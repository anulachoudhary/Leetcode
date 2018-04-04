# def unique_alphabet_count(string)
#     count = 0
#     alphabet_count = { }
#     for alphabet in string:
#         

# Given list of ints, return True if any two nums in list sum to 0.
# >>> add_to_zero([])
# False

# >>> add_to_zero([1])
# False

# >>> add_to_zero([1, 2, 3])
# False

# >>> add_to_zero([1, 2, 3, -2])
# True
# Given the wording of our problem, a zero in the list will always make this true, since “any two numbers” could include that same zero for both numbers, and they sum to zero:

# >>> add_to_zero([0, 1, 2])
# True


def add_to_zero(nums):

    for num in nums:
        if -num in set nums:
            return True

    return False
