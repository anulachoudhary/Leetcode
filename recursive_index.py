# Find the index of an item in a list using recursion.

# Given a list of items:
# >>> lst = ["hey", "there", "you"]

# You should have a function that returns the 0-based index of a sought item:
# >>> recursive_search("hey", lst)
# 0

# >>> recursive_search("you")
# 2

# If the item isn’t in the list, return None:
# >>> recursive_search("porcupine", lst) is None
# True


def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """

    # START SOLUTION

    def _recursive_index(needle, haystack, start_at):

        # Check if not found (we've gone too far)
        if start_at == len(haystack):
            return None

        # Have we found it?
        if haystack[start_at] == needle:
            return start_at

        return _recursive_index(needle, haystack, start_at + 1)

    return _recursive_index(needle, haystack, 0)