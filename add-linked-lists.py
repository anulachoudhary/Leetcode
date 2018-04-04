# There is a simple Node class for a linked list:

class Node(object):
    """Linked list node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_rev_string(self):
        """Represent data for this node and its successors as a string.

        >>> l1 = Node(3)
        >>> l1.as_rev_string()
        '3'

        >>> l1 = Node(3, Node(2, Node(1)))
        >>> l1.as_rev_string()
        '123'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(reversed(out))

# This includes a useful function for printing the contents of the list in reverse order. For example, if given a list of 3 → 2 → 1:

# >>> l1 = Node(3, Node(2, Node(1)))
# >>> l1.as_rev_string()
# '123'
# You will be given two linked lists in “reverse-digit” format. 
# For example, the number 123 would be given to you like this:
#  1 -> 2 -> 3 -> None


# And the number 456 like this:
#  6 -> 5 -> 4 -> None


# You should sum up these numbers You should return the sum of these two 
# numbers in the same “reverse-digit” format.

# For 123 + 456, this should return 579, in the form of a list like this:

#  9 -> 7 -> 5 -> None


def add_linked_lists(l1, l2):
    """Given two linked lists, treat like numbers and add together.

    l1: the head node of a linked list in "reverse-digit" format
    l2: the head node of another "reverse-digit" format

    Returns: head node of linked list of sum in "reverse-digit" format.
    """

    # START SOLUTION

    out_head = out_tail = None
    carried_over_digit = 0

    # Loop over both lists stopping when *both* lists are done

    while l1 or l2:

        # If not done l1, get digit, move to next. If done, use 0.

        if l1:
            digit1 = l1.data
            l1 = l1.next
        else:
            digit1 = 0

        # If not done l2, get digit, move to next. If done, use 0.

        if l2:
            digit2 = l2.data
            l2 = l2.next
        else:
            digit2 = 0

        # Add together digits (along w/carry) & determine new carry

        new_digit = digit1 + digit2 + carried_over_digit
        carried_over_digit, new_digit = divmod(new_digit, 10)

        # Add to end of our out LL

        if not out_head:
            out_head = out_tail = Node(new_digit)

        else:
            out_tail.next = Node(new_digit)
            out_tail = out_tail.next

    # If we have any carry left over, add a new place for it

    if carried_over_digit:
        out_tail.next = Node(carried_over_digit)

    return out_head