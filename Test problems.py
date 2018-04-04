# Test problems


class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node %s>" % self.data


class LinkedList(object):
    """Linked List using head and tail."""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        """Add node with data to end of list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node



# Given a single linkedlist. Each node has only strings. 
# Print the linkedlist in reverse order. 
def reverse_print(llist): 
    pass

# Given two linked lists, combine and create a new linkedlist
# To combine interleave items from each list
def combine_two_llists(llist1, llist2)
    pass

# Given a linked list with repeated data, create new one with unique data
def list_with_unique_data(llist3)
    pass

if __name__ == "__main__":

    llist1 = LinkedList()
    llist1.add_node("cherry")
    llist1.add_node("berry")
    llist1.add_node("apple")

    # llist2 = LinkedList()
    # llist2.add_node("boy")
    # llist2.add_node("girl")
    # llist2.add_node("man")
    
    # llist3 = LinkedList()
    # llist3.add_node("one")
    # llist3.add_node("two")
    # llist3.add_node("three")
    # llist3.add_node("two")
    # llist3.add_node("three")

    # reverse_print(llist)   ---> Output: apple, berry, cherry
    # combine_two_llists(llist1, llist2)     --->  apple, boy, berry, girl, etc. 
    # list_with_unique_data(llist3)     --->  one, two, three. 


    print "main"





# Hint for reverse_print - use an external data structure that can do this